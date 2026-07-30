"""
MRAT - Minimal Residual Attribution Test

Diagnostic routing layer for identifying the lowest-cost
structural source of empirical mismatch.

MRAT receives residual signals from PTVS and estimates:

    Φ_R(e_t) → (a_N, a_S, a_M, a_R, a_G)

where residuals are attributed across:

    N : Noise
    S : State error
    M : Mechanism deficit
    R : Representation saturation
    G : Generator decoupling

MRAT does not modify the system.
It only determines where mismatch originates.
"""

from .router import (
    MRATRouter,
    ResidualAttribution,
    AttributionClass,
)


__all__ = [
    "MRATRouter",
    "ResidualAttribution",
    "AttributionClass",
]
