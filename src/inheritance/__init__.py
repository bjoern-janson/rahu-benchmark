"""
Adaptive Inheritance Engine

Layer 3 of the Adaptive Intelligence architecture.

Maintains mechanism authority weights and applies
empirical attenuation when mechanisms lose contact
with environmental consequences.

Core invariant:

    E* ⇒ ∃ w_i ∈ W_invalid :
        dw_i / dt < 0

The inheritance layer answers:

    "When reality invalidates a mechanism,
     does that mechanism lose future authority?"
"""


from .engine import (
    InheritanceEngine,
    MechanismWeight,
)


__all__ = [
    "InheritanceEngine",
    "MechanismWeight",
]
