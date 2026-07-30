"""
Tests for MRAT Residual Attribution Layer.

MRAT invariant:

    observed failure
          |
          v
    residual attribution
          |
          v
    lowest-cost correction layer

The router should identify the smallest
structural layer capable of explaining
the contradiction.
"""


import pytest

from src.mrat.router import (
    MRATRouter,
)

from src.mrat.router import (
    Attribution,
)



def test_noise_residual_routes_to_noise():
    """
    Random observation errors should not
    trigger structural rewrites.
    """

    router = MRATRouter()


    residual = {
        "type": "observation_noise",
        "magnitude": 0.2,
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "noise"
    )



def test_state_error_routes_to_state():
    """
    Incorrect internal state estimates
    should update state handling.
    """

    router = MRATRouter()


    residual = {
        "type": "state_mismatch",
        "magnitude": 0.7,
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "state"
    )



def test_mechanism_failure_routes_correctly():
    """
    When the world model itself fails,
    mechanism authority should be targeted.
    """

    router = MRATRouter()


    residual = {
        "type": "mechanism_failure",
        "magnitude": 1.0,
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "mechanism"
    )



def test_representation_saturation_routes_to_representation():
    """
    A representation bottleneck should
    request representational change.
    """

    router = MRATRouter()


    residual = {
        "type": "representation_limit",
        "magnitude": 0.9,
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "representation"
    )



def test_generator_failure_routes_to_generator():
    """
    Highest-level failures should reach
    generator attribution.
    """

    router = MRATRouter()


    residual = {
        "type": "generator_failure",
        "magnitude": 1.0,
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "generator"
    )



def test_router_prefers_lower_cost_explanation():
    """
    MRAT should not jump to expensive
    explanations when simpler causes exist.
    """

    router = MRATRouter()


    residual = {
        "type": "ambiguous",
        "possible_causes": [
            {
                "layer": "noise",
                "cost": 0.1,
            },
            {
                "layer": "representation",
                "cost": 0.8,
            },
            {
                "layer": "generator",
                "cost": 1.0,
            },
        ],
    }


    result = router.attribute(
        residual
    )


    assert (
        result.layer
        ==
        "noise"
    )



def test_attribution_preserves_confidence():
    """
    Attribution should expose uncertainty.
    """

    router = MRATRouter()


    residual = {
        "type": "mechanism_failure",
    }


    result = router.attribute(
        residual
    )


    assert (
        0.0
        <=
        result.confidence
        <=
        1.0
    )
