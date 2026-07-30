"""
MRAT Router

Minimal Residual Attribution Test.

MRAT maps empirical residuals into competing
explanatory categories:

    Φ_R(e_t) → (a_N, a_S, a_M, a_R, a_G)

Categories:

    N:
        Noise / stochastic variation

    S:
        State estimation error

    M:
        Mechanism deficit

    R:
        Representation saturation

    G:
        Generator decoupling

MRAT is diagnostic only.
It does not update mechanisms.
"""


from dataclasses import dataclass
from enum import Enum
from typing import Dict


class AttributionClass(Enum):
    """
    Residual source categories.
    """

    NOISE = "noise"
    STATE = "state"
    MECHANISM = "mechanism"
    REPRESENTATION = "representation"
    GENERATOR = "generator"


@dataclass
class ResidualAttribution:
    """
    Output of the MRAT routing process.

    Values represent attribution confidence.

    Example:

        {
            noise: 0.8,
            mechanism: 0.1,
            representation: 0.1
        }

    """

    noise: float
    state: float
    mechanism: float
    representation: float
    generator: float

    def as_vector(self) -> Dict[str, float]:
        return {
            AttributionClass.NOISE.value:
                self.noise,

            AttributionClass.STATE.value:
                self.state,

            AttributionClass.MECHANISM.value:
                self.mechanism,

            AttributionClass.REPRESENTATION.value:
                self.representation,

            AttributionClass.GENERATOR.value:
                self.generator,
        }

    def dominant_source(self) -> AttributionClass:
        """
        Returns highest-probability attribution.
        """

        values = self.as_vector()

        source = max(
            values,
            key=values.get,
        )

        return AttributionClass(source)


class MRATRouter:
    """
    Residual attribution controller.

    Converts observed mismatch into a
    minimal structural explanation.

    The router follows:

        Φ_R(e_t)

    not:

        update(e_t)

    """

    def __init__(
        self,
        noise_threshold: float = 0.1,
        saturation_threshold: float = 0.8,
    ):
        self.noise_threshold = noise_threshold
        self.saturation_threshold = saturation_threshold


    def route(
        self,
        residual_error: float,
        expected_noise: float,
        representation_capacity: float,
        mechanism_failure_signal: float,
    ) -> ResidualAttribution:
        """
        Attribute residual source.

        Inputs:

            residual_error:
                observed contradiction magnitude

            expected_noise:
                predicted stochastic variation

            representation_capacity:
                remaining compression capacity

            mechanism_failure_signal:
                evidence current mechanism is invalid

        """

        noise = 0.0
        state = 0.0
        mechanism = 0.0
        representation = 0.0
        generator = 0.0


        # Noise explanation
        if residual_error <= expected_noise:
            noise = 1.0


        # Mechanism failure
        elif mechanism_failure_signal > 0.7:
            mechanism = (
                mechanism_failure_signal
            )


        # Representation saturation
        elif (
            representation_capacity
            < self.saturation_threshold
        ):
            representation = (
                1.0 - representation_capacity
            )


        # Default state mismatch
        else:
            state = 1.0


        return self._normalize(
            ResidualAttribution(
                noise=noise,
                state=state,
                mechanism=mechanism,
                representation=representation,
                generator=generator,
            )
        )


    def _normalize(
        self,
        attribution: ResidualAttribution,
    ) -> ResidualAttribution:
        """
        Normalize attribution vector to simplex.
        """

        values = attribution.as_vector()

        total = sum(values.values())

        if total == 0:
            return ResidualAttribution(
                noise=0.2,
                state=0.2,
                mechanism=0.2,
                representation=0.2,
                generator=0.2,
            )

        return ResidualAttribution(
            noise=values["noise"] / total,
            state=values["state"] / total,
            mechanism=values["mechanism"] / total,
            representation=values["representation"] / total,
            generator=values["generator"] / total,
        )
