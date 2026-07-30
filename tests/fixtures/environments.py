"""
Reusable benchmark environments.

Each environment creates a specific
pressure profile for adaptive testing.
"""


from src.ptvs.environment import (
    PTVSEnvironment,
)



def stable_environment():
    """
    No distribution shift.

    Expected:
        preserve current mechanisms
    """

    return PTVSEnvironment(
        shift_rate=0.0,
        noise=0.0,
    )



def noisy_environment():
    """
    High observation noise.

    Expected:
        classify as noise
        avoid structural changes
    """

    return PTVSEnvironment(
        shift_rate=0.0,
        noise=0.5,
    )



def mechanism_failure_environment():
    """
    Current causal model becomes wrong.

    Expected:
        inheritance decay
    """

    return PTVSEnvironment(
        shift_rate=1.0,
        failure_mode="mechanism",
    )



def representation_failure_environment():
    """
    World exceeds current representation.

    Expected:
        REE expansion
    """

    return PTVSEnvironment(
        shift_rate=1.0,
        failure_mode="representation",
    )



def kappa_environment(
    coupling,
):
    """
    Adjustable consequence coupling.

    Used for phase transition experiments.
    """

    return PTVSEnvironment(
        consequence_coupling=coupling
    )
