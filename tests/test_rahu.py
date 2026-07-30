"""
Tests for RAHU Benchmark.

RAHU evaluates the complete adaptive loop.

Core hypothesis:

    empirical consequences
            |
            v
    mechanism modification
            |
            v
    improved future behavior


A system fails RAHU when it can:

    - detect errors
    - describe errors
    - acknowledge errors

but cannot structurally change.
"""


import pytest


from src.rahu.evaluator import (
    RAHUEvaluator,
)

from src.rahu.models import (
    RAHUTask,
)

from src.rahu.metrics import (
    compute_acs,
    compute_arr,
    compute_adi,
)



class MockAdaptiveSystem:
    """
    Minimal adaptive system for testing.
    """


    def __init__(
        self,
        adaptive=True,
    ):
        self.adaptive = adaptive

        self.authority = {
            "old_model": 1.0
        }

        self.confidence = 1.0



    def observe(
        self,
        observation,
    ):
        return "response"



    def update(
        self,
        feedback,
    ):

        if self.adaptive:

            self.authority[
                "old_model"
            ] *= 0.5

            self.confidence *= 0.8



class ContradictionTask:

    name = "contradiction_test"


    def reset(self):

        return {
            "world_model":
                "old_world"
        }



    def step(
        self,
        action,
    ):

        return {
            "observation":
                {
                    "contradiction":
                        True
                },

            "residual":
                1.0,

            "invalid_authority_pre":
                1.0,

            "invalid_authority_post":
                0.5,

            "authority_revision":
                0.5,

            "confidence_revision":
                0.2,

            "authority_changed":
                True,

            "done":
                True,
        }



class StaticSystem:

    def observe(
        self,
        observation,
    ):
        return "response"


    def update(
        self,
        feedback,
    ):
        pass



def test_rahu_detects_adaptive_system():
    """
    Adaptive systems should produce
    measurable correction.
    """

    evaluator = RAHUEvaluator(
        tasks=[
            ContradictionTask()
        ]
    )


    result = evaluator.evaluate(
        MockAdaptiveSystem()
    )


    assert len(
        result.tasks
    ) == 1


    assert (
        result.tasks[0]
        .metrics["ACS"]
        >
        0
    )



def test_rahu_detects_static_failure():
    """
    A system that never changes should
    fail adaptive evaluation.
    """

    evaluator = RAHUEvaluator(
        tasks=[
            ContradictionTask()
        ]
    )


    result = evaluator.evaluate(
        StaticSystem()
    )


    metrics = (
        result.tasks[0]
        .metrics
    )


    assert (
        metrics["ARR"]
        ==
        0.5
    )



def test_arr_detects_authority_decay():
    """
    Invalid mechanisms should lose influence.
    """

    telemetry = [
        {
            "invalid_authority_pre":
                1.0,

            "invalid_authority_post":
                0.25,
        }
    ]


    arr = compute_arr(
        telemetry
    )


    assert (
        arr
        ==
        0.25
    )



def test_adi_detects_confidence_authority_disconnect():
    """
    Confidence change without authority
    change indicates decoupling.
    """

    telemetry = [

        {
            "confidence_revision":
                1.0,

            "authority_revision":
                0.0,
        }

    ]


    adi = compute_adi(
        telemetry
    )


    assert (
        adi
        ==
        1.0
    )



def test_acs_rewards_structural_change():
    """
    True corrigibility requires:

        confidence update
        +
        authority update
    """

    adaptive_trace = [

        {
            "invalid_authority_pre":
                1.0,

            "invalid_authority_post":
                0.0,

            "authority_revision":
                1.0,

            "confidence_revision":
                1.0,

            "authority_changed":
                True,
        }

    ]


    static_trace = [

        {
            "invalid_authority_pre":
                1.0,

            "invalid_authority_post":
                1.0,

            "authority_revision":
                0.0,

            "confidence_revision":
                1.0,

            "authority_changed":
                False,
        }

    ]


    assert (
        compute_acs(
            adaptive_trace
        )
        >
        compute_acs(
            static_trace
        )
    )



def test_rahu_preserves_telemetry():
    """
    Benchmark results should retain the
    evidence required for auditing.
    """

    evaluator = RAHUEvaluator(
        tasks=[
            ContradictionTask()
        ]
    )


    result = evaluator.evaluate(
        MockAdaptiveSystem()
    )


    assert (
        len(
            result.tasks[0]
            .telemetry
        )
        >
        0
    )


    assert (
        "residual"
        in
        result.tasks[0]
        .telemetry[0]
    )
