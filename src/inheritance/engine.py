"""
Adaptive Inheritance Engine

Layer 3: Authority redistribution.

Maintains the operational influence of mechanisms
over time.

The engine implements:

    E* ⇒ ∃ w_i ∈ W_invalid :
        dw_i / dt < 0

The core question:

    "When reality contradicts a mechanism,
     does that mechanism lose authority?"

Stored information is preserved.
Operational control is redistributed.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
import math


@dataclass
class MechanismWeight:
    """
    Represents the operational authority
    of a single mechanism.
    """

    name: str

    weight: float

    initial_weight: float

    active: bool = True

    invalidated: bool = False


class InheritanceEngine:
    """
    Maintains mechanism authority distribution W_t.

    Responsibilities:

        - register mechanisms
        - attenuate invalid mechanisms
        - measure authority retention
        - track decay dynamics

    Does not:

        - detect contradictions
        - perform attribution
        - expand representations
    """

    def __init__(
        self,
        decay_rate: float = 0.1,
    ):
        self.decay_rate = decay_rate

        self.mechanisms: Dict[
            str,
            MechanismWeight
        ] = {}

        self.history: List[Dict[str, float]] = []


    def register_mechanism(
        self,
        name: str,
        initial_weight: float,
    ):
        """
        Add a mechanism to the authority landscape.
        """

        self.mechanisms[name] = MechanismWeight(
            name=name,
            weight=initial_weight,
            initial_weight=initial_weight,
        )


    def invalidate(
        self,
        mechanism_name: str,
    ):
        """
        Mark mechanism as empirically invalidated.

        Invalidation does not remove the mechanism.
        It only allows authority decay.
        """

        if mechanism_name in self.mechanisms:
            self.mechanisms[
                mechanism_name
            ].invalidated = True


    def update(
        self,
    ):
        """
        Apply one authority redistribution step.

        Invalid mechanisms decay.

        Valid mechanisms retain authority.
        """

        snapshot = {}

        for name, mechanism in self.mechanisms.items():

            if mechanism.invalidated:

                mechanism.weight *= (
                    1 -
                    self.decay_rate
                )

            snapshot[name] = mechanism.weight


        self.history.append(snapshot)

        return snapshot


    def authority_retention_ratio(
        self,
        mechanism_name: str,
    ) -> float:
        """
        Compute ARR.

            ARR =
            post invalid authority
            ----------------------
            pre invalid authority

        """

        mechanism = self.mechanisms[
            mechanism_name
        ]

        if mechanism.initial_weight == 0:
            return 0.0

        return (
            mechanism.weight /
            mechanism.initial_weight
        )


    def authority_half_life(
        self,
        mechanism_name: str,
    ) -> Optional[int]:
        """
        Estimate mechanism authority half-life.

        τ½_authority =
            first time weight <= 50%
            of initial authority
        """

        mechanism = self.mechanisms[
            mechanism_name
        ]

        target = (
            mechanism.initial_weight *
            0.5
        )

        weight = mechanism.initial_weight

        for step in range(
            1,
            10000,
        ):

            weight *= (
                1 -
                self.decay_rate
            )

            if weight <= target:
                return step

        return None


    def authority_distribution(
        self,
    ) -> Dict[str, float]:
        """
        Return current W_t.
        """

        return {
            name: mechanism.weight
            for name, mechanism
            in self.mechanisms.items()
        }


    def total_authority(
        self,
    ) -> float:
        """
        Sum of active mechanism authority.
        """

        return sum(
            mechanism.weight
            for mechanism
            in self.mechanisms.values()
        )
