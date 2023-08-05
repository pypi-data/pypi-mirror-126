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

"""Implementation of a reduced cost functional.

"""

import fenics


class ReducedCostFunctional:
    """The reduced cost functional for the optimization problem

    A class that represents an reduced cost functional of an optimal control problem, which
    is used to evaluate it.
    """

    def __init__(self, form_handler, state_problem):
        """Initialize the reduced cost functional

        Parameters
        ----------
        form_handler : cashocs._forms.ControlFormHandler
                the FormHandler object for the optimization problem
        state_problem : cashocs._pde_problems.StateProblem
                the StateProblem object corresponding to the state system
        """

        self.form_handler = form_handler
        self.state_problem = state_problem

    def evaluate(self):
        """Evaluates the reduced cost functional.

        First solves the state system, so that the state variables are up-to-date,
        and then evaluates the reduced cost functional by assembling the corresponding
        UFL form.

        Returns
        -------
        float
                the value of the reduced cost functional
        """

        self.state_problem.solve()

        val = fenics.assemble(self.form_handler.cost_functional_form)

        if self.form_handler.use_scalar_tracking:
            for j in range(self.form_handler.no_scalar_tracking_terms):
                scalar_integral_value = fenics.assemble(
                    self.form_handler.scalar_cost_functional_integrands[j]
                )
                self.form_handler.scalar_cost_functional_integrand_values[j].vector()[
                    :
                ] = scalar_integral_value

                val += (
                    self.form_handler.scalar_weights[j].vector()[0]
                    / 2
                    * pow(
                        scalar_integral_value
                        - self.form_handler.scalar_tracking_goals[j],
                        2,
                    )
                )

        return val
