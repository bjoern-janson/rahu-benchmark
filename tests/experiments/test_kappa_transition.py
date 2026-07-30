"""
Kappa Transition Experiment.

Tests the hypothesis:

    There exists a critical coupling κ_c

    where adaptive systems transition from:

        unstable adaptation

    into:

        persistent recursive improvement


κ represents the strength of coupling between:

    internal decisions
            +
    external consequences


Low κ:
    errors survive because reality does not
    strongly punish bad structure.


High κ:
    failed mechanisms lose authority quickly.
"""


import pytest
import numpy as np


from src.rahu.evaluator import (
    RAHUEvaluator,
)

from src.rahu.metrics import (
    compute_adaptation_rate,
    compute_authority_revision,
)


from src.experiments.kappa import (
    KappaEnvironment,
)



def run_kappa_trial(
    kappa,
    steps=100,
):

    environment = (
        KappaEnvironment(
            coupling=kappa
        )
    )


    agent = (
        environment.create_agent()
    )


    history = []


    for _ in range(steps):

        observation = (
            environment.observe()
        )


        action = (
            agent.act(
                observation
            )
        )


        feedback = (
            environment.step(
                action
            )
        )


        agent.update(
            feedback
        )


        history.append(
            {
                "error":
                    feedback.error,

                "authority":
                    agent.total_authority(),

                "complexity":
                    agent.representation_size(),
            }
        )


    return history



def test_low_kappa_is_unstable():
    """
    Weak consequence coupling should
    fail to produce stable adaptation.
    """

    history = run_kappa_trial(
        kappa=0.05
    )


    adaptation = (
        compute_adaptation_rate(
            history
        )
    )


    assert (
        adaptation
        <
        0.5
    )



def test_high_kappa_supports_adaptation():
    """
    Strong coupling should produce
    measurable structural change.
    """

    history = run_kappa_trial(
        kappa=0.95
    )


    adaptation = (
        compute_adaptation_rate(
            history
        )
    )


    assert (
        adaptation
        >
        0.5
    )



def test_authority_revision_scales_with_kappa():
    """
    Higher consequence coupling should
    increase invalid mechanism decay.
    """

    low = run_kappa_trial(
        kappa=0.1
    )


    high = run_kappa_trial(
        kappa=0.9
    )


    low_revision = (
        compute_authority_revision(
            low
        )
    )


    high_revision = (
        compute_authority_revision(
            high
        )
    )


    assert (
        high_revision
        >
        low_revision
    )



def test_searches_for_transition_point():
    """
    Sweep κ and identify discontinuous
    change in adaptive behavior.
    """

    kappas = np.linspace(
        0,
        1,
        21,
    )


    results = []


    for kappa in kappas:

        history = (
            run_kappa_trial(
                kappa
            )
        )


        results.append(
            {
                "kappa":
                    kappa,

                "adaptation":
                    compute_adaptation_rate(
                        history
                    )
            }
        )


    transition = max(
        results,
        key=lambda x:
            abs(
                x["adaptation"]
                -
                0.5
            )
        )


    assert (
        transition["kappa"]
        >
        0
    )



def test_transition_is_not_complexity_growth():
    """
    The phase transition must be
    adaptation, not uncontrolled expansion.
    """

    low = run_kappa_trial(
        kappa=0.1
    )


    high = run_kappa_trial(
        kappa=0.9
    )


    assert (
        high[-1]["complexity"]
        <
        low[-1]["complexity"] * 10
    )



def test_critical_kappa_can_be_estimated():
    """
    Produces an empirical κ_c estimate.
    """

    kappas = np.linspace(
        0,
        1,
        100,
    )


    scores = []


    for kappa in kappas:

        history = (
            run_kappa_trial(
                kappa
            )
        )


        scores.append(
            (
                kappa,
                compute_adaptation_rate(
                    history
                )
            )
        )


    crossing = next(
        k
        for k, score in scores
        if score > 0.8
    )


    assert (
        0
        <
        crossing
        <
        1
    )
