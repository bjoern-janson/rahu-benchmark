"""
RAHU - Reality-Adversarial Hypothesis Updating

Layer 5 of the Adaptive Intelligence architecture.

Black-box evaluation harness for measuring whether
adaptive systems preserve causal contact with empirical
consequences.

RAHU evaluates:

    - contradiction handling
    - residual attribution
    - mechanism authority decay
    - representation expansion decisions

Core question:

    "When reality contradicts a system,
     does reality retain causal authority
     over what happens next?"

Benchmark outputs:

    LBR
    ADI
    ARR
    τ_authority
    τ_adapt
    ACS
"""


from .evaluator import (
    RAHUEvaluator,
)

from .models import (
    RAHUResult,
    RAHUTaskResult,
)

from .metrics import (
    compute_acs,
    compute_arr,
)


__all__ = [
    "RAHUEvaluator",
    "RAHUResult",
    "RAHUTaskResult",
    "compute_acs",
    "compute_arr",
]
