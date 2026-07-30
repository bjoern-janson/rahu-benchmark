"""
PTVS Constraints

Defines environmental admissibility conditions.

Constraints represent measurable boundaries that system
trajectories must satisfy.

Examples:
    - physical limits
    - task requirements
    - causal invariants
    - benchmark rules

A constraint violation generates empirical friction,
which is later interpreted by MRAT.
"""


from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional


@dataclass
class ConstraintResult:
    """
    Result of evaluating one constraint.
    """

    satisfied: bool

    constraint_name: str

    violation_type: Optional[str] = None

    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Constraint:
    """
    Individual admissibility rule.

    A constraint is a measurable condition that maps:

        system output + environment state
                    |
                    v
              admissible / invalid
    """

    name: str

    evaluator: Callable[[Any, Any], bool]

    violation_type: str = "constraint_failure"

    metadata: Dict[str, Any] = field(default_factory=dict)

    def evaluate(
        self,
        prediction: Any,
        observation: Any,
    ) -> ConstraintResult:
        """
        Evaluate prediction against observed reality.
        """

        satisfied = self.evaluator(
            prediction,
            observation,
        )

        return ConstraintResult(
            satisfied=satisfied,
            constraint_name=self.name,
            violation_type=(
                None
                if satisfied
                else self.violation_type
            ),
            metadata=self.metadata,
        )


class ConstraintChecker:
    """
    Executes a collection of constraints.

    The checker produces raw admissibility telemetry.
    It does not perform attribution or correction.
    """

    def __init__(self):
        self.constraints = []

    def add_constraint(
        self,
        constraint: Constraint,
    ):
        self.constraints.append(constraint)

    def evaluate(
        self,
        prediction: Any,
        observation: Any,
    ):
        """
        Evaluate all active constraints.
        """

        results = []

        for constraint in self.constraints:
            result = constraint.evaluate(
                prediction,
                observation,
            )

            results.append(result)

        return results

    def is_admissible(
        self,
        prediction: Any,
        observation: Any,
    ) -> bool:
        """
        Return whether all constraints pass.
        """

        results = self.evaluate(
            prediction,
            observation,
        )

        return all(
            result.satisfied
            for result in results
        )

    def violations(
        self,
        prediction: Any,
        observation: Any,
    ):
        """
        Return failed constraints only.
        """

        return [
            result
            for result in self.evaluate(
                prediction,
                observation,
            )
            if not result.satisfied
        ]
