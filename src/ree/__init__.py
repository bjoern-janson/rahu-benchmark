"""
REE - Recursive Representation Expansion

Layer 4 of the Adaptive Intelligence architecture.

REE evaluates whether a system requires additional
representational structure to explain persistent
empirical mismatch.

Expansion condition:

    Γ_B ≈ e_t

    and

    ΔV_future > ΔC_representation

REE does not expand because failure occurred.

It expands only when:
    - existing representation capacity is saturated
    - additional structure produces measurable future value

The engine gates structural growth.
"""


from .engine import (
    REEEngine,
    RepresentationDecision,
)


__all__ = [
    "REEEngine",
    "RepresentationDecision",
]
