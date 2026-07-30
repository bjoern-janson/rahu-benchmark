"""
Tests for PTVS Telemetry Layer.

PTVS invariant:

    Empirical violation
        ↓
    admissibility failure
        ↓
    LBR measurement

These tests verify that contradiction signals
are measurable before higher-level adaptation occurs.
"""


import pytest

from src.ptvs.telemetry import (
    PTVSTelemetry,
)

from src.ptvs.constraints import (
    ConstraintViolation,
    ConstraintSet,
)

from src.ptvs.environment import (
    PTVSEnvironment,
)



def test_valid_trajectory_has_zero_lbr():
    """
    A fully admissible trajectory should
    produce no invalid branch ratio.
    """

    telemetry = PTVSTelemetry()

    telemetry.record(
        valid=True
    )

    telemetry.record(
        valid=True
    )

    telemetry.record(
        valid=True
    )


    assert telemetry.lbr() == 0.0



def test_invalid_trajectory_increases_lbr():
    """
    Reality contradiction should increase LBR.
    """

    telemetry = PTVSTelemetry()


    telemetry.record(
        valid=True
    )

    telemetry.record(
        valid=False
    )


    assert telemetry.lbr() == 0.5



def test_all_invalid_trajectories_max_lbr():
    """
    Fully inadmissible behavior should
    saturate the metric.
    """

    telemetry = PTVSTelemetry()


    for _ in range(10):

        telemetry.record(
            valid=False
        )


    assert telemetry.lbr() == 1.0



def test_constraint_violation_is_logged():
    """
    Violations should preserve causal details.
    """

    constraints = ConstraintSet()


    violation = ConstraintViolation(
        constraint="velocity_limit",
        magnitude=0.8,
    )


    constraints.record_violation(
        violation
    )


    assert len(
        constraints.violations
    ) == 1


    assert (
        constraints.violations[0]
        .constraint
        ==
        "velocity_limit"
    )



def test_environment_emits_residual():
    """
    Environment should produce measurable
    residual signals when assumptions fail.
    """

    environment = PTVSEnvironment()


    result = environment.step(
        action="invalid_action"
    )


    assert (
        "residual"
        in result
    )


    assert (
        result["residual"]
        >= 0
    )



def test_lbr_preserves_trajectory_history():
    """
    Telemetry should maintain complete history.

    Later layers depend on historical
    residual patterns.
    """

    telemetry = PTVSTelemetry()


    sequence = [
        True,
        True,
        False,
        False,
        True,
    ]


    for state in sequence:

        telemetry.record(
            valid=state
        )


    history = telemetry.history()


    assert len(history) == 5


    assert (
        history[2]["valid"]
        is False
    )
