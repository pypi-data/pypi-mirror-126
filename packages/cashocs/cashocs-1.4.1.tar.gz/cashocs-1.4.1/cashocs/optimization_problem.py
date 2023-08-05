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

"""Blueprints for the PDE constrained optimization problems.

This module is used to define the parent class for the optimization problems,
as many parameters and variables are common for optimal control and shape
optimization problems.
"""

import configparser
import copy
import json

import fenics
import numpy as np
import ufl
from ufl import replace

from ._exceptions import InputError
from ._forms import FormHandler, Lagrangian
from ._loggers import info, warning
from ._pde_problems import StateProblem
from .utils import (
    _parse_remesh,
    summation,
    _check_and_enlist_functions,
    _check_and_enlist_ufl_forms,
    _check_and_enlist_bcs,
    _check_and_enlist_ksp_options,
    _optimization_algorithm_configuration,
)


class OptimizationProblem:
    """Blueprint for an abstract PDE constrained optimization problem.

    This class performs the initialization of the shared input so that the rest
    of CASHOCS can use it directly. Additionally, it includes methods that
    can be used to compute the state and adjoint variables by solving the
    corresponding equations. This could be subclassed to generate custom
    optimization problems.
    """

    def __init__(
        self,
        state_forms,
        bcs_list,
        cost_functional_form,
        states,
        adjoints,
        config=None,
        initial_guess=None,
        ksp_options=None,
        adjoint_ksp_options=None,
        desired_weights=None,
        scalar_tracking_forms=None,
    ):
        r"""Initializes the optimization problem.

        Parameters
        ----------
        state_forms : ufl.form.Form or list[ufl.form.Form]
                The weak form of the state equation (user implemented). Can be either
                a single UFL form, or a (ordered) list of UFL forms.
        bcs_list : list[dolfin.fem.dirichletbc.DirichletBC] or list[list[dolfin.fem.dirichletbc.DirichletBC]] or dolfin.fem.dirichletbc.DirichletBC or None
                The list of :py:class:`fenics.DirichletBC` objects describing Dirichlet (essential) boundary conditions.
                If this is ``None``, then no Dirichlet boundary conditions are imposed.
        cost_functional_form : ufl.form.Form or list[ufl.form.Form]
                UFL form of the cost functional. Can also be a list of individual terms of the cost functional,
                which are scaled according to desired_weights.
        states : dolfin.function.function.Function or list[dolfin.function.function.Function]
                The state variable(s), can either be a :py:class:`fenics.Function`, or a list of these.
        adjoints : dolfin.function.function.Function or list[dolfin.function.function.Function]
                The adjoint variable(s), can either be a :py:class:`fenics.Function`, or a (ordered) list of these.
        config : configparser.ConfigParser or None
                The config file for the problem, generated via :py:func:`cashocs.create_config`.
                Alternatively, this can also be ``None``, in which case the default configurations
                are used, except for the optimization algorithm. This has then to be specified
                in the :py:meth:`solve <cashocs.OptimalControlProblem.solve>` method. The
                default is ``None``.
        initial_guess : list[dolfin.function.function.Function], optional
                List of functions that act as initial guess for the state variables, should be valid input for :py:func:`fenics.assign`.
                Defaults to ``None``, which means a zero initial guess.
        ksp_options : list[list[str]] or list[list[list[str]]] or None, optional
                A list of strings corresponding to command line options for PETSc,
                used to solve the state systems. If this is ``None``, then the direct solver
                mumps is used (default is ``None``).
        adjoint_ksp_options : list[list[str]] or list[list[list[str]]] or None
                A list of strings corresponding to command line options for PETSc,
                used to solve the adjoint systems. If this is ``None``, then the same options
                as for the state systems are used (default is ``None``).
        desired_weights : list[int] or list[float] or None:
                A list which indicates the value of the associated term in the cost functional on
                the initial geometry in case a list of cost functions is supplied. If this is ``None``,
                this defaults to multiplying all terms and adding them.
        scalar_tracking_forms : dict or list[dict] or None
                A list of dictionaries that define scalar tracking type cost functionals,
                where an integral value should be brought to a desired value. Each dict needs
                to have the keys ``'integrand'`` and ``'tracking_goal'``. Default is ``None``,
                i.e., no scalar tracking terms are considered.

        Notes
        -----
        If one uses a single PDE constraint, the inputs can be the objects
        (UFL forms, functions, etc.) directly. In case multiple PDE constraints
        are present the inputs have to be put into (ordered) lists. The order of
        the objects depends on the order of the state variables, so that
        ``state_forms[i]`` is the weak form of the PDE for ``states[i]`` with boundary
        conditions ``bcs_list[i]`` and corresponding adjoint state ``adjoints[i]``.

        See Also
        --------
        cashocs.OptimalControlProblem : Represents an optimal control problem.
        cashocs.ShapeOptimizationProblem : Represents a shape optimization problem.
        """

        self.has_cashocs_remesh_flag, self.temp_dir = _parse_remesh()

        ### state_forms
        try:
            self.state_forms = _check_and_enlist_ufl_forms(state_forms)
        except:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "state_forms",
                "Type of state_forms is wrong.",
            )

        self.state_dim = len(self.state_forms)

        ### bcs_list
        if bcs_list == [] or bcs_list is None:
            self.bcs_list = []
            for i in range(self.state_dim):
                self.bcs_list.append([])
        else:
            try:
                self.bcs_list = _check_and_enlist_bcs(bcs_list)
            except InputError:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "bcs_list",
                    "Type of bcs_list is wrong.",
                )

        ### cost_functional_form
        self.use_cost_functional_list = False
        if isinstance(cost_functional_form, list):
            self.use_cost_functional_list = True

        try:
            self.cost_functional_form_list = _check_and_enlist_ufl_forms(
                cost_functional_form
            )
            if self.use_cost_functional_list:
                self.cost_functional_list = self.cost_functional_form_list
                self.cost_functional_form = summation(self.cost_functional_form_list)
            else:
                self.cost_functional_form = self.cost_functional_form_list[0]
        except InputError:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "cost_functional_form",
                "Type of cost_functional_form is wrong.",
            )

        ### states
        try:
            self.states = _check_and_enlist_functions(states)
        except InputError:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "states",
                "Type of states is wrong.",
            )

        ### adjoints
        try:
            self.adjoints = _check_and_enlist_functions(adjoints)
        except InputError:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "adjoints",
                "Type of adjoints is wrong.",
            )

        ### config
        if config is None:
            self.config = configparser.ConfigParser()
            self.config.add_section("OptimizationRoutine")
            self.config.set("OptimizationRoutine", "algorithm", "none")
        else:
            try:
                if isinstance(config, configparser.ConfigParser):
                    self.config = copy.deepcopy(config)
                else:
                    raise InputError(
                        "cashocs.optimization_problem.OptimizationProblem",
                        "config",
                        "config has to be of configparser.ConfigParser type",
                    )
            except AttributeError:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "config",
                    "config has to be of configparser.ConfigParser type",
                )

        ### initial guess
        if initial_guess is None:
            self.initial_guess = initial_guess
        else:
            try:
                self.initial_guess = _check_and_enlist_functions(initial_guess)
            except InputError:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "initial_guess",
                    "Type of initial_guess is wrong.",
                )

        ### ksp_options
        if ksp_options is None:
            self.ksp_options = []
            option = [
                ["ksp_type", "preonly"],
                ["pc_type", "lu"],
                ["pc_factor_mat_solver_type", "mumps"],
                ["mat_mumps_icntl_24", 1],
            ]

            for i in range(self.state_dim):
                self.ksp_options.append(option)
        else:
            try:
                self.ksp_options = _check_and_enlist_ksp_options(ksp_options)
            except InputError:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "ksp_options",
                    "Type of ksp_options is wrong.",
                )

        ### adjoint_ksp_options
        if adjoint_ksp_options is None:
            self.adjoint_ksp_options = self.ksp_options[:]

        else:
            try:
                self.adjoint_ksp_options = _check_and_enlist_ksp_options(
                    adjoint_ksp_options
                )
            except InputError:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "adjoint_ksp_options",
                    "Type of adjoint_ksp_options is wrong.",
                )

        ### desired_weights
        if desired_weights is not None:
            if isinstance(desired_weights, list):
                for weight in desired_weights:
                    if not isinstance(weight, (float, int)):
                        raise InputError(
                            "cashocs.optimization_problem.OptimizationProblem",
                            "desired_weights",
                            "desired_weights needs to be a list of numbers (int or float).",
                        )

                self.desired_weights = desired_weights

            else:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "desired_weights",
                    "desired_weights needs to be a list of numbers (int or float).",
                )
        else:
            self.desired_weights = None

        ### scalar_tracking_forms
        self.use_scalar_tracking = False
        self.scalar_cost_functional_integrands = None
        self.scalar_tracking_goals = None

        if scalar_tracking_forms is None:
            self.scalar_tracking_forms = scalar_tracking_forms
        else:
            try:
                if isinstance(scalar_tracking_forms, list):
                    for term in scalar_tracking_forms:
                        if isinstance(term, dict):
                            if ("integrand" in term.keys()) and (
                                "tracking_goal" in term.keys()
                            ):
                                pass
                            else:
                                raise InputError(
                                    "cashocs.optimization_problem.OptimizationProblem",
                                    "scalar_tracking_forms",
                                    "each dict in scalar_tracking_forms has to have the keys 'integrand' and 'tracking_goal'",
                                )
                        else:
                            raise InputError(
                                "cashocs.optimization_problem.OptimizationProblem",
                                "scalar_tracking_forms",
                                "scalar_tracking_forms has to be a dict or a list of dicts.",
                            )

                    self.scalar_tracking_forms = scalar_tracking_forms
                    self.use_scalar_tracking = True

                elif isinstance(scalar_tracking_forms, dict):
                    if ("integrand" in scalar_tracking_forms.keys()) and (
                        "tracking_goal" in scalar_tracking_forms.keys()
                    ):
                        pass
                    else:
                        raise InputError(
                            "cashocs.optimization_problem.OptimizationProblem",
                            "scalar_tracking_forms",
                            "each dict in scalar_tracking_forms has to have the keys 'integrand' and 'tracking_goal'",
                        )

                    self.scalar_tracking_forms = [scalar_tracking_forms]
                    self.use_scalar_tracking = True

                else:
                    raise InputError(
                        "cashocs.optimization_problem.OptimizationProblem",
                        "scalar_tracking_forms",
                        "scalar_tracking_forms has to be a dict or list of dicts.",
                    )
            except:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "scalar_tracking_forms",
                    "Type of scalar_tracking_forms is wrong.",
                )

        if not len(self.bcs_list) == self.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "bcs_list",
                "Length of states does not match.",
            )
        if not len(self.states) == self.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "states",
                "Length of states does not match.",
            )
        if not len(self.adjoints) == self.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "adjoints",
                "Length of states does not match.",
            )

        if self.initial_guess is not None:
            if not len(self.initial_guess) == self.state_dim:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "initial_guess",
                    "Length of states does not match.",
                )

        if not len(self.ksp_options) == self.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "ksp_options",
                "Length of states does not match.",
            )
        if not len(self.adjoint_ksp_options) == self.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "ksp_options",
                "Length of states does not match.",
            )

        if self.desired_weights is not None:
            try:
                if not self.use_scalar_tracking:
                    if not len(self.cost_functional_list) == len(self.desired_weights):
                        raise InputError(
                            "cashocs.optimization_problem.OptimizationProblem",
                            "desired_weights",
                            "Length of desired_weights and cost_functional does not match.",
                        )
                else:
                    if self.use_cost_functional_list:
                        if not len(self.desired_weights) == (
                            len(self.cost_functional_list)
                            + len(self.scalar_tracking_forms)
                        ):
                            raise InputError(
                                "cashocs.optimization_problem.OptimizationProblem",
                                "desired_weights",
                                "Length of desired_weights and cost_functional and scalar_tracking_forms does not match.",
                            )
                    else:
                        if (
                            not len(self.desired_weights)
                            == len(self.scalar_tracking_forms) + 1
                        ):
                            raise InputError(
                                "cashocs.optimization_problem.OptimizationProblem",
                                "desired_weights",
                                "Length of desired_weights and cost_functional and scalar_tracking_forms does not match.",
                            )
            except:
                raise InputError(
                    "cashocs.optimization_problem.OptimizationProblem",
                    "desired_weights",
                    "Length of desired_weights and cost_functional does not match.",
                )

        self.bool_scaling = False
        if self.desired_weights is not None:
            self.bool_scaling = True

        fenics.set_log_level(fenics.LogLevel.CRITICAL)

        self.state_problem = None
        self.adjoint_problem = None

        self.lagrangian = Lagrangian(
            self.state_forms, self.cost_functional_form, self.scalar_tracking_forms
        )
        self.form_handler = None
        self.has_custom_adjoint = False
        self.has_custom_derivative = False

        self.uses_custom_scalar_product = False

        self._scale_cost_functional()

    def compute_state_variables(self):
        """Solves the state system.

        This can be used for debugging purposes and to validate the solver.
        Updates and overwrites the user input for the state variables.

        Returns
        -------
        None
        """

        self.state_problem.solve()

    def compute_adjoint_variables(self):
        """Solves the adjoint system.

        This can be used for debugging purposes and solver validation.
        Updates / overwrites the user input for the adjoint variables.
        The solve of the corresponding state system needed to determine
        the adjoints is carried out automatically.

        Returns
        -------
        None
        """

        self.state_problem.solve()
        self.adjoint_problem.solve()

    def supply_adjoint_forms(self, adjoint_forms, adjoint_bcs_list):
        """Overrides the computed weak forms of the adjoint system.

        This allows the user to specify their own weak forms of the problems and to use cashocs merely as
        a solver for solving the optimization problems.

        Parameters
        ----------
        adjoint_forms : ufl.form.Form or list[ufl.form.Form]
                The UFL forms of the adjoint system(s).
        adjoint_bcs_list : list[dolfin.fem.dirichletbc.DirichletBC] or list[list[dolfin.fem.dirichletbc.DirichletBC]] or dolfin.fem.dirichletbc.DirichletBC or None
                The list of Dirichlet boundary conditions for the adjoint system(s).

        Returns
        -------
        None
        """

        try:
            if isinstance(adjoint_forms, list) and len(adjoint_forms) > 0:
                for i in range(len(adjoint_forms)):
                    if isinstance(adjoint_forms[i], ufl.form.Form):
                        pass
                    else:
                        raise InputError(
                            "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                            "adjoint_forms",
                            "adjoint_forms have to be ufl forms",
                        )
                mod_forms = adjoint_forms
            elif isinstance(adjoint_forms, ufl.form.Form):
                mod_forms = [adjoint_forms]
            else:
                raise InputError(
                    "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                    "adjoint_forms",
                    "adjoint_forms have to be ufl forms",
                )
        except:
            raise InputError(
                "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                "adjoint_forms",
                "adjoint_forms have to be ufl forms",
            )

        try:
            if adjoint_bcs_list == [] or adjoint_bcs_list is None:
                mod_bcs_list = []
                for i in range(self.state_dim):
                    mod_bcs_list.append([])
            elif isinstance(adjoint_bcs_list, list) and len(adjoint_bcs_list) > 0:
                if isinstance(adjoint_bcs_list[0], list):
                    for i in range(len(adjoint_bcs_list)):
                        if isinstance(adjoint_bcs_list[i], list):
                            pass
                        else:
                            raise InputError(
                                "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                                "adjoint_bcs_list",
                                "adjoint_bcs_list has inconsistent types.",
                            )
                    mod_bcs_list = adjoint_bcs_list

                elif isinstance(adjoint_bcs_list[0], fenics.DirichletBC):
                    for i in range(len(adjoint_bcs_list)):
                        if isinstance(adjoint_bcs_list[i], fenics.DirichletBC):
                            pass
                        else:
                            raise InputError(
                                "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply adjoint_forms",
                                "adjoint_bcs_list",
                                "adjoint_bcs_list has inconsistent types.",
                            )
                    mod_bcs_list = [adjoint_bcs_list]
            elif isinstance(adjoint_bcs_list, fenics.DirichletBC):
                mod_bcs_list = [[adjoint_bcs_list]]
            else:
                raise InputError(
                    "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                    "adjoint_bcs_list",
                    "Type of adjoint_bcs_list is wrong.",
                )
        except:
            raise InputError(
                "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                "adjoint_bcs_list",
                "Type of adjoint_bcs_list is wrong.",
            )

        if not len(mod_forms) == self.form_handler.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem.supply_adjoint_forms",
                "adjoint_forms",
                "Length of adjoint_forms does not match",
            )
        if not len(mod_bcs_list) == self.form_handler.state_dim:
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem.supply_adjoint_forms",
                "adjoint_bcs_list",
                "Length of adjoint_bcs_list does not match",
            )

        for idx, form in enumerate(mod_forms):
            if len(form.arguments()) == 2:
                raise InputError(
                    "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                    "adjoint_forms",
                    "Do not use TrialFunction for the adjoints, but the actual Function you passed to th OptimalControlProblem.",
                )
            elif len(form.arguments()) == 0:
                raise InputError(
                    "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                    "adjoint_forms",
                    "The specified adjoint_forms must include a TestFunction object.",
                )

            if (
                not form.arguments()[0].ufl_function_space()
                == self.form_handler.adjoint_spaces[idx]
            ):
                raise InputError(
                    "cashocs._shape_optimization.shape_optimization_problem.ShapeOptimizationProblem.supply_adjoint_forms",
                    "adjoint_forms",
                    "The TestFunction has to be chosen from the same space as the corresponding adjoint.",
                )

        self.form_handler.adjoint_picard_forms = mod_forms
        self.form_handler.bcs_list_ad = mod_bcs_list

        # replace the adjoint function by a TrialFunction for internal use
        repl_forms = [
            replace(
                mod_forms[i],
                {self.adjoints[i]: self.form_handler.trial_functions_adjoint[i]},
            )
            for i in range(self.state_dim)
        ]
        self.form_handler.adjoint_eq_forms = repl_forms

        self.form_handler.adjoint_eq_lhs = []
        self.form_handler.adjoint_eq_rhs = []

        for i in range(self.state_dim):
            a, L = fenics.system(self.form_handler.adjoint_eq_forms[i])
            self.form_handler.adjoint_eq_lhs.append(a)
            if L.empty():
                zero_form = (
                    fenics.inner(
                        fenics.Constant(
                            np.zeros(
                                self.form_handler.test_functions_adjoint[i].ufl_shape
                            )
                        ),
                        self.form_handler.test_functions_adjoint[i],
                    )
                    * self.form_handler.dx
                )
                self.form_handler.adjoint_eq_rhs.append(zero_form)
            else:
                self.form_handler.adjoint_eq_rhs.append(L)

        self.has_custom_adjoint = True

    def _check_for_custom_forms(self):
        """Checks whether custom user forms are used and if they are compatible with the settings.

        Returns
        -------
        None
        """

        if self.has_custom_adjoint and not self.has_custom_derivative:
            warning(
                "You only supplied the adjoint system. This might lead to unexpected results.\n"
                "Consider also supplying the (shape) derivative of the reduced cost functional,"
                "or check your approach with the cashocs.verification module."
            )

        elif not self.has_custom_adjoint and self.has_custom_derivative:
            warning(
                "You only supplied the derivative of the reduced cost functional. This might lead to unexpected results.\n"
                "Consider also supplying the adjoint system, "
                "or check your approach with the cashocs.verification module."
            )

        if self.algorithm == "newton" and (
            self.has_custom_adjoint or self.has_custom_derivative
        ):
            raise InputError(
                "cashocs.optimization_problem.OptimizationProblem",
                "solve",
                "The usage of custom forms is not compatible with the Newton solver."
                "Please do not supply custom forms if you want to use the Newton solver.",
            )

        if self.bool_scaling:
            info(
                "You use the automatic scaling functionality of cashocs. This might lead to unexpected results if you try to scale the cost functional yourself.\n"
                "You can check your approach with the cashocs.verification module."
            )

    def _scale_cost_functional(self):

        if self.bool_scaling:

            if not self.has_cashocs_remesh_flag:
                # Create dummy objects for adjoints, so that we can actually solve the state problem
                temp_form_handler = FormHandler(self)
                temp_state_problem = StateProblem(temp_form_handler, self.initial_guess)

                temp_state_problem.solve()
                self.initial_function_values = []
                if self.use_cost_functional_list:
                    for i in range(len(self.cost_functional_list)):
                        val = fenics.assemble(self.cost_functional_list[i])

                        if abs(val) <= 1e-15:
                            val = 1.0
                            info(
                                f"Term {i:d} of the cost functional vanishes for the initial iteration. Multiplying this term with the factor you supplied in desired_weights."
                            )

                        self.initial_function_values.append(val)

                else:
                    val = fenics.assemble(self.cost_functional_form)
                    if abs(val) <= 1e-15:
                        val = 1.0
                        info(
                            "The cost functional vanishes for the initial iteration. Multiplying this term with the factor you supplied in desired_weights."
                        )

                    self.initial_function_values.append(val)

                if self.use_scalar_tracking:
                    self.initial_scalar_tracking_values = []
                    for i in range(len(self.scalar_tracking_forms)):
                        val = 0.5 * pow(
                            fenics.assemble(
                                temp_form_handler.scalar_cost_functional_integrands[i]
                            )
                            - temp_form_handler.scalar_tracking_goals[i],
                            2,
                        )

                        if abs(val) <= 1e-15:
                            val = 1.0
                            info(
                                f"Term {i:d} of the scalar tracking cost functional vanishes for the initial iteration. Multiplying this term with the factor you supplied in desired_weights."
                            )

                        self.initial_scalar_tracking_values.append(val)

            else:
                with open(f"{self.temp_dir}/temp_dict.json", "r") as file:
                    temp_dict = json.load(file)
                self.initial_function_values = temp_dict["initial_function_values"]
                if self.use_scalar_tracking:
                    self.initial_scalar_tracking_values = temp_dict[
                        "initial_scalar_tracking_values"
                    ]

            if self.use_cost_functional_list:
                self.cost_functional_form = summation(
                    [
                        fenics.Constant(
                            abs(
                                self.desired_weights[i]
                                / self.initial_function_values[i]
                            )
                        )
                        * self.cost_functional_list[i]
                        for i in range(len(self.cost_functional_list))
                    ]
                )
            else:
                self.cost_functional_form = (
                    fenics.Constant(
                        abs(self.desired_weights[0] / self.initial_function_values[0])
                    )
                    * self.cost_functional_form
                )

            if self.use_scalar_tracking:
                for i in range(len(self.scalar_tracking_forms)):
                    self.scalar_tracking_forms[-1 - i]["weight"] = abs(
                        self.desired_weights[-1 - i]
                        / self.initial_scalar_tracking_values[-1 - i]
                    )

            self.lagrangian = Lagrangian(
                self.state_forms, self.cost_functional_form, self.scalar_tracking_forms
            )

        else:
            if self.use_cost_functional_list:
                self.cost_functional_form = summation(
                    [term for term in self.cost_functional_list]
                )

    def inject_pre_hook(self, function):
        """
        Changes the a-priori hook of the OptimizationProblem

        Parameters
        ----------
        function : function
            A custom function without arguments, which will be called before each solve
            of the state system

        Returns
        -------
         : None

        """

        self.form_handler._pre_hook = function
        self.state_problem.has_solution = False
        self.adjoint_problem.has_solution = False
        try:
            self.gradient_problem.has_solution = False
        except AttributeError:
            self.shape_gradient_problem.has_solution = False

    def inject_post_hook(self, function):
        """
        Changes the a-posteriori hook of the OptimizationProblem

        Parameters
        ----------
        function : function
            A custom function without arguments, which will be called after the computation
            of the gradient(s)

        Returns
        -------
         : None

        """

        self.form_handler._post_hook = function
        self.state_problem.has_solution = False
        self.adjoint_problem.has_solution = False
        try:
            self.gradient_problem.has_solution = False
        except AttributeError:
            self.shape_gradient_problem.has_solution = False

    def inject_pre_post_hook(self, pre_function, post_function):
        """
        Changes the a-priori (pre) and a-posteriori (post) hook of the OptimizationProblem

        Parameters
        ----------
        pre_function : function
            A function without arguments, which is to be called before each solve of the
            state system
        post_function : function
            A function without arguments, which is to be called after each computation of
            the (shape) gradient

        Returns
        -------
         : None

        """

        self.inject_pre_hook(pre_function)
        self.inject_post_hook(post_function)

    def solve(self, algorithm=None, rtol=None, atol=None, max_iter=None):
        r"""Solves the optimization problem by the method specified in the config file.

        Parameters
        ----------
        algorithm : str or None, optional
                Selects the optimization algorithm. Valid choices are
                ``'gradient_descent'`` or ``'gd'`` for a gradient descent method,
                ``'conjugate_gradient'``, ``'nonlinear_cg'``, ``'ncg'`` or ``'cg'``
                for nonlinear conjugate gradient methods, and ``'lbfgs'`` or ``'bfgs'`` for
                limited memory BFGS methods. This overwrites the value specified
                in the config file. If this is ``None``, then the value in the
                config file is used. Default is ``None``. In addition, for optimal control problems,
                one can use ``'newton'`` for a truncated Newton method,
                and ``'pdas'`` or ``'primal_dual_active_set'`` for a
                primal dual active set method.
        rtol : float or None, optional
                The relative tolerance used for the termination criterion.
                Overwrites the value specified in the config file. If this
                is ``None``, the value from the config file is taken. Default
                is ``None``.
        atol : float or None, optional
                The absolute tolerance used for the termination criterion.
                Overwrites the value specified in the config file. If this
                is ``None``, the value from the config file is taken. Default
                is ``None``.
        max_iter : int or None, optional
                The maximum number of iterations the optimization algorithm
                can carry out before it is terminated. Overwrites the value
                specified in the config file. If this is ``None``, the value from
                the config file is taken. Default is ``None``.

        Returns
        -------
        None

        Notes
        -----
        If either ``rtol`` or ``atol`` are specified as arguments to the solve
        call, the termination criterion changes to:

          - a purely relative one (if only ``rtol`` is specified), i.e.,

          .. math:: || \nabla J(u_k) || \leq \texttt{rtol} || \nabla J(u_0) ||.

          - a purely absolute one (if only ``atol`` is specified), i.e.,

          .. math:: || \nabla J(u_K) || \leq \texttt{atol}.

          - a combined one if both ``rtol`` and ``atol`` are specified, i.e.,

          .. math:: || \nabla J(u_k) || \leq \texttt{atol} + \texttt{rtol} || \nabla J(u_0) ||
        """

        self.algorithm = _optimization_algorithm_configuration(self.config, algorithm)

        if (rtol is not None) and (atol is None):
            self.config.set("OptimizationRoutine", "rtol", str(rtol))
            self.config.set("OptimizationRoutine", "atol", str(0.0))
        elif (atol is not None) and (rtol is None):
            self.config.set("OptimizationRoutine", "rtol", str(0.0))
            self.config.set("OptimizationRoutine", "atol", str(atol))
        elif (atol is not None) and (rtol is not None):
            self.config.set("OptimizationRoutine", "rtol", str(rtol))
            self.config.set("OptimizationRoutine", "atol", str(atol))

        if max_iter is not None:
            self.config.set("OptimizationRoutine", "maximum_iterations", str(max_iter))

        self._check_for_custom_forms()
