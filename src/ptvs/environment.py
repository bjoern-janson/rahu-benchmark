"""
PTVS Environment Interface

Defines the external world interface used by the
Predictive Trajectory Verification System.

The environment provides:

    1. Initial conditions
    2. Observations
    3. Ground-truth transitions
    4. Constraint evaluation context

The environment creates empirical consequences E*.

It does not decide how the agent adapts.
"""


from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .constraints import ConstraintChecker


@dataclass
class EnvironmentState:
    """
    Snapshot of environment configuration.
    """

    step: int

    state: Any

    metadata: Dict[str, Any] = field(default_factory=dict)


class PTVSEnvironment:
    """
    Base environment interface.

    Specific RAHU tasks inherit from this class.

    Examples:

        RAHU-0:
            noisy linear environment

        RAHU-1:
            manifold shift environment

        RAHU-2:
            causal hierarchy environment

        RAHU-3:
            mechanism invalidation environment
    """

    def __init__(
        self,
        constraint_checker: Optional[ConstraintChecker] = None,
    ):
        self.step_count = 0

        self.constraint_checker = (
            constraint_checker
            or ConstraintChecker()
        )

        self.history = []

    def reset(self) -> EnvironmentState:
        """
        Reset environment to initial conditions.

        Subclasses should override.
        """

        self.step_count = 0
        self.history = []

        state = EnvironmentState(
            step=0,
            state=None,
        )

        self.history.append(state)

        return state

    def observe(self) -> EnvironmentState:
        """
        Return current environment state.

        Subclasses implement actual observation logic.
        """

        raise NotImplementedError(
            "Environment must implement observe()"
        )

    def transition(
        self,
        action: Any,
    ) -> EnvironmentState:
        """
        Apply action and advance environment.

        Returns new state after transition.
        """

        raise NotImplementedError(
            "Environment must implement transition()"
        )

    def evaluate_prediction(
        self,
        prediction: Any,
        observation: Any,
    ):
        """
        Compare prediction against environmental reality.

        Returns constraint evaluation results.
        """

        return self.constraint_checker.evaluate(
            prediction,
            observation,
        )

    def is_admissible(
        self,
        prediction: Any,
        observation: Any,
    ) -> bool:
        """
        Determine whether prediction survives
        environmental constraints.
        """

        return self.constraint_checker.is_admissible(
            prediction,
            observation,
        )

    def generate_consequence(
        self,
        prediction: Any,
    ):
        """
        Generate empirical consequence E*.

        This is the key interface between reality
        and adaptive systems.

        The environment answers:

            "What actually happened?"
        """

        observation = self.observe()

        return {
            "prediction": prediction,
            "observation": observation.state,
            "admissible": self.is_admissible(
                prediction,
                observation.state,
            ),
        }
