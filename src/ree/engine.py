"""
REE - Recursive Representation Expansion Engine

Layer 4: Structural expansion gating.

REE determines whether a system should expand
its representational capacity.

Core conditions:

    Γ_B ≈ e_t

    and

    ΔV_future > ΔC_representation


Failure alone is insufficient.

Expansion occurs only when:

    1. Current representation cannot compress
       persistent residuals.

    2. Additional structure provides greater
       expected future adaptive value than its cost.

REE prevents uncontrolled complexity growth.
"""


from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ExpansionDecision(Enum):
    """
    Possible REE outcomes.
    """

    MAINTAIN = "maintain"
    EXPAND = "expand"
    REJECT = "reject"


@dataclass
class RepresentationDecision:
    """
    Output of REE gating.

    Contains the evidence behind
    representation changes.
    """

    decision: ExpansionDecision

    compressibility_gap: float

    future_value_gain: float

    representation_cost: float

    justification: str



class REEEngine:
    """
    Recursive Representation Expansion controller.

    Responsibilities:

        - estimate representation saturation
        - compare expansion value vs cost
        - gate structural growth

    Does not:

        - detect failures
        - attribute residuals
        - modify mechanism weights
    """

    def __init__(
        self,
        saturation_threshold: float = 0.9,
    ):
        self.saturation_threshold = (
            saturation_threshold
        )


    def evaluate(
        self,
        residual_error: float,
        max_budget_compressibility: float,
        expected_future_value: float,
        representation_cost: float,
    ) -> RepresentationDecision:
        """
        Evaluate whether representation expansion
        is admissible.

        Parameters:

            residual_error:
                observed contradiction magnitude

            max_budget_compressibility:
                maximum residual reduction possible
                under current representation

            expected_future_value:
                predicted benefit from expansion

            representation_cost:
                computational / structural cost
        """

        compressibility_gap = (
            residual_error -
            max_budget_compressibility
        )


        saturated = (
            compressibility_gap
            > self.saturation_threshold
        )


        worthwhile = (
            expected_future_value
            >
            representation_cost
        )


        if saturated and worthwhile:

            return RepresentationDecision(
                decision=ExpansionDecision.EXPAND,

                compressibility_gap=(
                    compressibility_gap
                ),

                future_value_gain=(
                    expected_future_value
                ),

                representation_cost=(
                    representation_cost
                ),

                justification=(
                    "Current representation "
                    "cannot compress residual "
                    "and expansion has positive "
                    "expected adaptive value."
                ),
            )


        if not saturated:

            return RepresentationDecision(
                decision=ExpansionDecision.MAINTAIN,

                compressibility_gap=(
                    compressibility_gap
                ),

                future_value_gain=(
                    expected_future_value
                ),

                representation_cost=(
                    representation_cost
                ),

                justification=(
                    "Residual remains "
                    "compressible under "
                    "current representation."
                ),
            )


        return RepresentationDecision(
            decision=ExpansionDecision.REJECT,

            compressibility_gap=(
                compressibility_gap
            ),

            future_value_gain=(
                expected_future_value
            ),

            representation_cost=(
                representation_cost
            ),

            justification=(
                "Expansion cost exceeds "
                "expected future value."
            ),
        )


    def expansion_admissible(
        self,
        decision: RepresentationDecision,
    ) -> bool:
        """
        Convenience check for downstream systems.
        """

        return (
            decision.decision
            ==
            ExpansionDecision.EXPAND
        )
