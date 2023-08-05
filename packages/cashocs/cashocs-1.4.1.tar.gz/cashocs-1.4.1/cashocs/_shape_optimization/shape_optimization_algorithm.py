# Copyright (C) 2020-2021 Sebastian Blauth
#
# This file is part of CASHOCS.
#
# CASHOCS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CASHOCS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CASHOCS.  If not, see <https://www.gnu.org/licenses/>.

"""Blueprints for shape optimization algorithms.

"""

import json
import subprocess

import fenics

from .._exceptions import NotConvergedError
from .._loggers import error, info
from .._optimization_algorithm import OptimizationAlgorithm
from ..utils import write_out_mesh


class ShapeOptimizationAlgorithm(OptimizationAlgorithm):
    """Blueprint for a solution algorithm for shape optimization problems"""

    def __init__(self, optimization_problem):
        """Parent class for the optimization methods implemented in cashocs.optimization.methods

        Parameters
        ----------
        optimization_problem : cashocs.ShapeOptimizationProblem
                the optimization problem
        """

        super().__init__(optimization_problem)

        self.line_search_broken = False
        self.requires_remeshing = False
        self.remeshing_its = False
        self.has_curvature_info = False

        self.mesh_handler = optimization_problem.mesh_handler

        self.shape_gradient_problem = optimization_problem.shape_gradient_problem
        self.gradient = self.shape_gradient_problem.gradient
        self.search_direction = fenics.Function(self.form_handler.deformation_space)

        self.temp_dict = optimization_problem.temp_dict
        if self.mesh_handler.do_remesh:
            if not self.config.getboolean("Debug", "remeshing", fallback=False):
                self.temp_dir = optimization_problem.temp_dir
        if self.config.getboolean("Mesh", "remesh", fallback=False):
            self.iteration = self.temp_dict["OptimizationRoutine"].get(
                "iteration_counter", 0
            )
        else:
            self.iteration = 0

        self.output_dict = dict()
        try:
            self.output_dict["cost_function_value"] = self.temp_dict["output_dict"][
                "cost_function_value"
            ]
            self.output_dict["gradient_norm"] = self.temp_dict["output_dict"][
                "gradient_norm"
            ]
            self.output_dict["stepsize"] = self.temp_dict["output_dict"]["stepsize"]
            self.output_dict["MeshQuality"] = self.temp_dict["output_dict"][
                "MeshQuality"
            ]
        except (TypeError, KeyError):
            self.output_dict["cost_function_value"] = []
            self.output_dict["gradient_norm"] = []
            self.output_dict["stepsize"] = []
            self.output_dict["MeshQuality"] = []

        if self.save_pvd:
            self.state_pvd_list = []
            for i in range(self.form_handler.state_dim):
                if (
                    self.form_handler.state_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.state_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    self.state_pvd_list.append([])
                    for j in range(self.form_handler.state_spaces[i].num_sub_spaces()):
                        if self.mesh_handler.do_remesh:
                            self.state_pvd_list[i].append(
                                fenics.File(
                                    f"{self.result_dir}/pvd/remesh_{self.temp_dict.get('remesh_counter', 0):d}_state_{i:d}_{j:d}.pvd"
                                )
                            )
                        else:
                            self.state_pvd_list[i].append(
                                fenics.File(
                                    f"{self.result_dir}/pvd/state_{i:d}_{j:d}.pvd"
                                )
                            )
                else:
                    if self.mesh_handler.do_remesh:
                        self.state_pvd_list.append(
                            fenics.File(
                                f"{self.result_dir}/pvd/remesh_{self.temp_dict.get('remesh_counter', 0):d}_state_{i:d}.pvd"
                            )
                        )
                    else:
                        self.state_pvd_list.append(
                            fenics.File(f"{self.result_dir}/pvd/state_{i:d}.pvd")
                        )

        if self.save_pvd_adjoint:
            self.adjoint_pvd_list = []
            for i in range(self.form_handler.state_dim):
                if (
                    self.form_handler.adjoint_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.adjoint_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    self.adjoint_pvd_list.append([])
                    for j in range(
                        self.form_handler.adjoint_spaces[i].num_sub_spaces()
                    ):
                        if self.mesh_handler.do_remesh:
                            self.adjoint_pvd_list[i].append(
                                fenics.File(
                                    f"{self.result_dir}/pvd/remesh_{self.temp_dict.get('remesh_counter', 0):d}_adjoint_{i:d}_{j:d}.pvd"
                                )
                            )
                        else:
                            self.adjoint_pvd_list[i].append(
                                fenics.File(
                                    f"{self.result_dir}/pvd/adjoint_{i:d}_{j:d}.pvd"
                                )
                            )
                else:
                    if self.mesh_handler.do_remesh:
                        self.adjoint_pvd_list.append(
                            fenics.File(
                                f"{self.result_dir}/pvd/remesh_{self.temp_dict.get('remesh_counter', 0):d}_adjoint_{i:d}.pvd"
                            )
                        )
                    else:
                        self.adjoint_pvd_list.append(
                            fenics.File(f"{self.result_dir}/pvd/adjoint_{i:d}.pvd")
                        )

        if self.save_pvd_gradient:
            if self.mesh_handler.do_remesh:
                self.shape_gradient_pvd_file = fenics.File(
                    f"{self.result_dir}/pvd/remesh_{self.temp_dict.get('remesh_counter', 0):d}_shape_gradient.pvd"
                )

            else:
                self.shape_gradient_pvd_file = fenics.File(
                    f"{self.result_dir}/pvd/shape_gradient.pvd"
                )

    def print_results(self):
        """Prints the current state of the optimization algorithm to the console.

        Returns
        -------
        None
        """

        if self.iteration == 0:
            output = (
                f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Gradient norm:  {self.gradient_norm_initial:.3e} (abs)"
                + f"    Mesh Quality: {self.mesh_handler.current_mesh_quality:1.2f} ({self.mesh_handler.mesh_quality_measure})\n"
            )

        else:
            output = (
                f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Gradient norm:  {self.relative_norm:.3e} (rel)"
                + f"    Mesh Quality: {self.mesh_handler.current_mesh_quality:1.2f} ({self.mesh_handler.mesh_quality_measure})    Step size:  {self.stepsize:.3e}"
            )

        self.output_dict["cost_function_value"].append(self.objective_value)
        self.output_dict["gradient_norm"].append(self.relative_norm)
        self.output_dict["stepsize"].append(self.stepsize)
        self.output_dict["MeshQuality"].append(self.mesh_handler.current_mesh_quality)

        if self.save_pvd:
            for i in range(self.form_handler.state_dim):
                if (
                    self.form_handler.state_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.state_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    for j in range(self.form_handler.state_spaces[i].num_sub_spaces()):
                        self.state_pvd_list[i][j] << (
                            self.form_handler.states[i].sub(j, True),
                            float(self.iteration),
                        )
                else:
                    self.state_pvd_list[i] << (
                        self.form_handler.states[i],
                        float(self.iteration),
                    )

        if self.save_pvd_adjoint:
            for i in range(self.form_handler.state_dim):
                if (
                    self.form_handler.adjoint_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.adjoint_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    for j in range(
                        self.form_handler.adjoint_spaces[i].num_sub_spaces()
                    ):
                        self.adjoint_pvd_list[i][j] << (
                            self.form_handler.adjoints[i].sub(j, True),
                            float(self.iteration),
                        )
                else:
                    self.adjoint_pvd_list[i] << (
                        self.form_handler.adjoints[i],
                        float(self.iteration),
                    )

        if self.save_pvd_gradient:
            self.shape_gradient_pvd_file << self.gradient, float(self.iteration)

        if self.verbose:
            print(output)

        if self.save_txt:
            if self.iteration == 0:
                with open(f"{self.result_dir}/history.txt", "w") as file:
                    file.write(f"{output}\n")
            else:
                with open(f"{self.result_dir}/history.txt", "a") as file:
                    file.write(f"{output}\n")

    def print_summary(self):
        """Prints a summary of the (successful) optimization to console

        Returns
        -------
        None
        """

        output = (
            f"\nStatistics --- Total iterations: {self.iteration:4d} --- Final objective value:  {self.objective_value:.3e} --- Final gradient norm:  {self.relative_norm:.3e} (rel)\n"
            + f"           --- State equations solved: {self.state_problem.number_of_solves:d} --- Adjoint equations solved: {self.adjoint_problem.number_of_solves}\n"
        )
        if self.verbose:
            print(output)

        if self.save_txt:
            with open(f"{self.result_dir}/history.txt", "a") as file:
                file.write(output)

    def finalize(self):
        """Saves the history of the optimization algorithm

        Returns
        -------
        None
        """

        self.output_dict["initial_gradient_norm"] = self.gradient_norm_initial
        self.output_dict["state_solves"] = self.state_problem.number_of_solves
        self.output_dict["adjoint_solves"] = self.adjoint_problem.number_of_solves
        self.output_dict["iterations"] = self.iteration
        if self.save_results:
            with open(f"{self.result_dir}/history.json", "w") as file:
                json.dump(self.output_dict, file)

        if self.mesh_handler.save_optimized_mesh:
            write_out_mesh(
                self.mesh_handler.mesh,
                self.mesh_handler.gmsh_file,
                f"{self.result_dir}/optimized_mesh.msh",
            )

        if self.mesh_handler.do_remesh:
            if not self.config.getboolean("Debug", "remeshing", fallback=False):
                subprocess.run(["rm", "-r", self.temp_dir], check=True)
                subprocess.run(
                    ["rm", "-r", self.mesh_handler.remesh_directory], check=True
                )

    def run(self):
        """Blueprint run method, overriden by the actual solution algorithms

        Returns
        -------
        None
        """

        pass

    def post_processing(self):
        """Post processing of the solution algorithm

        Makes sure that the finalize method is called and that the output is written
        to files.

        Returns
        -------
        None
        """

        if self.converged:
            self.print_results()
            self.print_summary()
            self.finalize()

        else:
            # maximum iterations reached
            if self.converged_reason == -1:
                self.print_results()
                if self.soft_exit:
                    if self.verbose:
                        print("Maximum number of iterations exceeded.")
                    self.finalize()
                else:
                    self.finalize()
                    raise NotConvergedError(
                        "Optimization Algorithm",
                        "Maximum number of iterations were exceeded.",
                    )

            # Armijo line search failed
            elif self.converged_reason == -2:
                self.iteration -= 1
                if self.soft_exit:
                    if self.verbose:
                        print("Armijo rule failed.")
                    self.finalize()
                else:
                    self.finalize()
                    raise NotConvergedError(
                        "Armijo line search",
                        "Failed to compute a feasible Armijo step.",
                    )

            # Mesh Quality is too low
            elif self.converged_reason == -3:
                self.iteration -= 1
                if self.mesh_handler.do_remesh:
                    info("Mesh quality too low. Performing a remeshing operation.\n")
                    self.mesh_handler.remesh(self)
                else:
                    if self.soft_exit:
                        error("Mesh quality is too low.")
                        self.finalize()
                    else:
                        self.finalize()
                        raise NotConvergedError(
                            "Optimization Algorithm", "Mesh quality is too low."
                        )

            # Iteration for remeshing is the one exceeding the maximum number of iterations
            elif self.converged_reason == -4:
                if self.soft_exit:
                    if self.verbose:
                        print("Maximum number of iterations exceeded.")
                    self.finalize()
                else:
                    self.finalize()
                    raise NotConvergedError(
                        "Optimization Algorithm",
                        "Maximum number of iterations were exceeded.",
                    )

    def nonconvergence(self):
        """Checks for nonconvergence of the solution algorithm

        Returns
        -------
         : boolean
                A flag which is True, when the algorithm did not converge
        """

        if self.iteration >= self.maximum_iterations:
            self.converged_reason = -1
        if self.line_search_broken:
            self.converged_reason = -2
        if self.requires_remeshing:
            self.converged_reason = -3
        if self.remeshing_its:
            self.converged_reason = -4

        if self.converged_reason < 0:
            return True
        else:
            return False
