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

"""Blueprint for the optimization algorithms.

"""

import json

import fenics
import numpy as np

from .._exceptions import NotConvergedError
from .._optimization_algorithm import OptimizationAlgorithm


class ControlOptimizationAlgorithm(OptimizationAlgorithm):
    """Abstract class representing a optimization algorithm

    This is used for subclassing with the specific optimization methods
    later on.

    See Also
    --------
    methods.gradient_descent.GradientDescent
    methods.cg.CG
    methods.l_bfgs.LBFGS
    methods.newton.Newton
    methods.primal_dual_active_set_method.PDAS
    """

    def __init__(self, optimization_problem):
        """Initializes the optimization algorithm

        Defines common parameters used by all sub-classes.

        Parameters
        ----------
        optimization_problem : cashocs._optimal_control.optimal_control_problem.OptimalControlProblem
                the OptimalControlProblem class as defined through the user
        """

        super().__init__(optimization_problem)

        self.gradient_problem = optimization_problem.gradient_problem
        self.gradients = optimization_problem.gradients
        self.controls = optimization_problem.controls
        self.controls_temp = [
            fenics.Function(V) for V in optimization_problem.control_spaces
        ]
        self.projected_difference = [
            fenics.Function(V) for V in optimization_problem.control_spaces
        ]
        self.search_directions = [
            fenics.Function(V) for V in optimization_problem.control_spaces
        ]

        self.require_control_constraints = (
            optimization_problem.require_control_constraints
        )

        self.iteration = 0

        self.pdas_solver = False

        self.output_dict = dict()
        self.output_dict["cost_function_value"] = []
        self.output_dict["gradient_norm"] = []
        self.output_dict["stepsize"] = []

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
                        self.state_pvd_list[i].append(
                            fenics.File(f"{self.result_dir}/pvd/state_{i:d}_{j:d}.pvd")
                        )
                else:
                    self.state_pvd_list.append(
                        fenics.File(f"{self.result_dir}/pvd/state_{i:d}.pvd")
                    )

            self.control_pvd_list = []
            for i in range(self.form_handler.control_dim):
                if (
                    self.form_handler.control_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.control_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    self.control_pvd_list.append([])
                    for j in range(
                        self.form_handler.control_spaces[i].num_sub_spaces()
                    ):
                        self.control_pvd_list[i].append(
                            fenics.File(
                                f"{self.result_dir}/pvd/control_{i:d}_{j:d}.pvd"
                            )
                        )
                else:
                    self.control_pvd_list.append(
                        fenics.File(f"{self.result_dir}/pvd/control_{i:d}.pvd")
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
                        self.adjoint_pvd_list[i].append(
                            fenics.File(
                                f"{self.result_dir}/pvd/adjoint_{i:d}_{j:d}.pvd"
                            )
                        )
                else:
                    self.adjoint_pvd_list.append(
                        fenics.File(f"{self.result_dir}/pvd/adjoint_{i:d}.pvd")
                    )

        if self.save_pvd_gradient:
            self.gradient_pvd_list = []
            for i in range(self.form_handler.control_dim):
                if (
                    self.form_handler.control_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.control_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    self.gradient_pvd_list.append([])
                    for j in range(
                        self.form_handler.control_spaces[i].num_sub_spaces()
                    ):
                        self.gradient_pvd_list[i].append(
                            fenics.File(
                                f"{self.result_dir}/pvd/gradient_{i:d}_{j:d}.pvd"
                            )
                        )
                else:
                    self.gradient_pvd_list.append(
                        fenics.File(f"{self.result_dir}/pvd/gradient_{i:d}.pvd")
                    )

    def _stationary_measure_squared(self):
        """Computes the stationary measure (squared) corresponding to box-constraints

        In case there are no box constraints this reduces to the classical gradient
        norm.

        Returns
        -------
         float
                The square of the stationary measure

        """

        for j in range(self.form_handler.control_dim):
            self.projected_difference[j].vector()[:] = (
                self.controls[j].vector()[:] - self.gradients[j].vector()[:]
            )

        self.form_handler.project_to_admissible_set(self.projected_difference)

        for j in range(self.form_handler.control_dim):
            self.projected_difference[j].vector()[:] = (
                self.controls[j].vector()[:] - self.projected_difference[j].vector()[:]
            )

        return self.form_handler.scalar_product(
            self.projected_difference, self.projected_difference
        )

    def print_results(self):
        """Prints the current state of the optimization algorithm to the console.

        Returns
        -------
        None
        """
        if not np.any(self.require_control_constraints):
            if self.iteration == 0:
                output = f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Gradient norm:  {self.gradient_norm_initial:.3e} (abs) \n"
            else:
                output = f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Gradient norm:  {self.relative_norm:.3e} (rel)    Step size:  {self.stepsize:.3e}"

        else:
            if self.iteration == 0:
                output = f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Stationarity measure:  {self.gradient_norm_initial:.3e} (abs) \n"
            else:
                output = f"Iteration {self.iteration:4d} - Objective value:  {self.objective_value:.3e}    Stationarity measure:  {self.relative_norm:.3e} (rel)    Step size:  {self.stepsize:.3e}"

        self.output_dict["cost_function_value"].append(self.objective_value)
        self.output_dict["gradient_norm"].append(self.relative_norm)
        self.output_dict["stepsize"].append(self.stepsize)

        if self.save_pvd:
            for i in range(self.form_handler.state_dim):
                if (
                    self.form_handler.state_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.state_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    for j in range(self.form_handler.state_spaces[i].num_sub_spaces()):
                        self.state_pvd_list[i][j] << self.form_handler.states[i].sub(
                            j, True
                        ), self.iteration
                else:
                    self.state_pvd_list[i] << self.form_handler.states[
                        i
                    ], self.iteration

            for i in range(self.form_handler.control_dim):
                if (
                    self.form_handler.control_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.control_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    for j in range(
                        self.form_handler.control_spaces[i].num_sub_spaces()
                    ):
                        self.control_pvd_list[i][j] << self.form_handler.controls[
                            i
                        ].sub(j, True), self.iteration
                else:
                    self.control_pvd_list[i] << self.form_handler.controls[
                        i
                    ], self.iteration

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
                        self.adjoint_pvd_list[i][j] << self.form_handler.adjoints[
                            i
                        ].sub(j, True), self.iteration
                else:
                    self.adjoint_pvd_list[i] << self.form_handler.adjoints[
                        i
                    ], self.iteration

        if self.save_pvd_gradient:
            for i in range(self.form_handler.control_dim):
                if (
                    self.form_handler.control_spaces[i].num_sub_spaces() > 0
                    and self.form_handler.control_spaces[i].ufl_element().family()
                    == "Mixed"
                ):
                    for j in range(
                        self.form_handler.control_spaces[i].num_sub_spaces()
                    ):
                        self.gradient_pvd_list[i][j] << self.gradients[i].sub(
                            j, True
                        ), self.iteration
                else:
                    self.gradient_pvd_list[i] << self.gradients[i], self.iteration

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
        """Prints a summary of the optimization to console.

        Returns
        -------
        None
        """

        output = (
            f"\nStatistics -- Total iterations: {self.iteration:4d} --- Final objective value:  {self.objective_value:.3e} --- Final gradient norm:  {self.relative_norm:.3e} (rel)\n"
            + f"           --- State equations solved: {self.state_problem.number_of_solves:d} --- Adjoint equations solved: {self.adjoint_problem.number_of_solves:d}\n"
        )

        if self.verbose:
            print(output)

        if self.save_txt:
            with open(f"{self.result_dir}/history.txt", "a") as file:
                file.write(output)

    def finalize(self):
        """Finalizes the solution algorithm.

        This saves the history of the optimization into the .json file.
        Called after the solver has finished.

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

    def run(self):
        """Blueprint for a print function

        This is overrriden by the specific optimization algorithms later on.

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

        if self.converged_reason < 0:
            return True
        else:
            return False
