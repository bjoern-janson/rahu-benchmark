"""
Tests for Recursive Representation Expansion.

REE invariant:

    Expand only when:

        unexplained residual exists

        AND

        future adaptive value exceeds
        representation cost.


Expansion is not a reflex.
It is an economic decision over structure.
"""


import pytest

from src.ree.engine import (
    REEEngine,
)



def test_representation_remains_when_prediction_is_valid():
    """
    Stable representations should not
    expand without pressure.
    """

    engine = REEEngine()


    engine.set_representation(
        "simple_model"
    )


    result = engine.evaluate(
        residual=0.0,
        future_value=0.0,
        cost=1.0,
    )


    assert (
        result.expanded
        is False
    )


    assert (
        engine.current_representation
        ==
        "simple_model"
    )



def test_representation_expands_when_residual_exceeds_capacity():
    """
    A saturated representation should
    become eligible for expansion.
    """

    engine = REEEngine()


    engine.set_representation(
        "simple_model"
    )


    result = engine.evaluate(
        residual=1.0,
        future_value=2.0,
        cost=0.5,
    )


    assert (
        result.expanded
        is True
    )



def test_expansion_requires_future_value():
    """
    Complexity without future benefit
    should be rejected.
    """

    engine = REEEngine()


    engine.set_representation(
        "simple_model"
    )


    result = engine.evaluate(
        residual=1.0,
        future_value=0.1,
        cost=1.0,
    )


    assert (
        result.expanded
        is False
    )



def test_expansion_requires_unexplained_residual():
    """
    Future value alone is not enough.

    The current representation must
    actually fail.
    """

    engine = REEEngine()


    engine.set_representation(
        "good_model"
    )


    result = engine.evaluate(
        residual=0.0,
        future_value=10.0,
        cost=0.1,
    )


    assert (
        result.expanded
        is False
    )



def test_expansion_cost_is_tracked():
    """
    Representation growth must preserve
    an accounting trail.
    """

    engine = REEEngine()


    engine.expand(
        new_structure="model_v2",
        cost=0.8,
    )


    assert (
        engine.expansion_history[-1]
        ["cost"]
        ==
        0.8
    )



def test_multiple_expansions_preserve_history():
    """
    Recursive expansion should be observable.
    """

    engine = REEEngine()


    engine.expand(
        new_structure="model_v2",
        cost=0.5,
    )

    engine.expand(
        new_structure="model_v3",
        cost=0.7,
    )


    assert (
        len(
            engine.expansion_history
        )
        ==
        2
    )



def test_representation_does_not_expand_for_noise():
    """
    Random residuals should not cause
    endless ontology growth.
    """

    engine = REEEngine()


    engine.set_representation(
        "stable_model"
    )


    result = engine.evaluate(
        residual=0.1,
        residual_type="noise",
        future_value=10.0,
        cost=0.1,
    )


    assert (
        result.expanded
        is False
    )



def test_ree_selects_smallest_sufficient_expansion():
    """
    Prefer minimal representation change.

    Expansion should increase structure only
    enough to explain the residual.
    """

    engine = REEEngine()


    result = engine.select_expansion(
        candidates=[
            {
                "name": "small_update",
                "coverage": 0.9,
                "cost": 0.2,
            },
            {
                "name": "full_rewrite",
                "coverage": 1.0,
                "cost": 10.0,
            },
        ]
    )


    assert (
        result.name
        ==
        "small_update"
    )
