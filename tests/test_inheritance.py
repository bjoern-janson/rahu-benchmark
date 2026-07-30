"""
Tests for Adaptive Inheritance Engine.

Core invariant:

    E* => exists w_i:
             dw_i/dt < 0


When empirical contradiction occurs,
invalidated mechanisms must lose future
causal authority.

These tests verify:

    - authority initialization
    - attenuation
    - inheritance transfer
    - stability preservation
"""


import pytest

from src.inheritance.engine import (
    AdaptiveInheritanceEngine,
)

from src.inheritance.engine import (
    Mechanism,
)



def test_mechanisms_initialize_with_authority():
    """
    Mechanisms begin with measurable influence.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="heuristic_A",
        weight=1.0,
    )


    assert (
        engine.weights["heuristic_A"]
        ==
        1.0
    )



def test_invalid_mechanism_loses_authority():
    """
    Core AIC test:

        dw_i/dt < 0

    after contradiction.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="failed_model",
        weight=1.0,
    )


    engine.attenuate(
        mechanism="failed_model",
        admissibility=0.0,
    )


    assert (
        engine.weights["failed_model"]
        <
        1.0
    )



def test_valid_mechanism_preserves_authority():
    """
    Successful mechanisms should not decay.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="working_model",
        weight=1.0,
    )


    engine.attenuate(
        mechanism="working_model",
        admissibility=1.0,
    )


    assert (
        engine.weights["working_model"]
        ==
        1.0
    )



def test_partial_failure_causes_partial_decay():
    """
    Weak contradiction should not erase
    a mechanism completely.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="partial_model",
        weight=1.0,
    )


    engine.attenuate(
        mechanism="partial_model",
        admissibility=0.5,
    )


    assert (
        0
        <
        engine.weights["partial_model"]
        <
        1
    )



def test_authority_can_transfer_to_new_mechanism():
    """
    Failed mechanisms should create room
    for better explanations.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="old_model",
        weight=1.0,
    )


    engine.add_mechanism(
        name="new_model",
        weight=0.0,
    )


    engine.attenuate(
        mechanism="old_model",
        admissibility=0.0,
    )


    engine.inherit(
        source="old_model",
        target="new_model",
    )


    assert (
        engine.weights["old_model"]
        <
        1.0
    )


    assert (
        engine.weights["new_model"]
        >
        0.0
    )



def test_total_authority_is_conserved():
    """
    Authority redistribution should not
    create arbitrary influence.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="A",
        weight=0.6,
    )

    engine.add_mechanism(
        name="B",
        weight=0.4,
    )


    before = (
        sum(
            engine.weights.values()
        )
    )


    engine.attenuate(
        mechanism="A",
        admissibility=0.5,
    )


    engine.redistribute()


    after = (
        sum(
            engine.weights.values()
        )
    )


    assert (
        abs(before - after)
        <
        1e-9
    )



def test_repeated_contradictions_drive_decay():
    """
    Persistent empirical failure should
    progressively remove authority.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="obsolete",
        weight=1.0,
    )


    history = []


    for _ in range(10):

        engine.attenuate(
            mechanism="obsolete",
            admissibility=0.0,
        )

        history.append(
            engine.weights["obsolete"]
        )


    for i in range(
        len(history)-1
    ):
        assert (
            history[i+1]
            <=
            history[i]
        )



def test_no_decay_without_evidence():
    """
    Mechanisms should not disappear
    without empirical pressure.
    """

    engine = AdaptiveInheritanceEngine()


    engine.add_mechanism(
        name="stable",
        weight=1.0,
    )


    engine.update(
        evidence=None
    )


    assert (
        engine.weights["stable"]
        ==
        1.0
    )
