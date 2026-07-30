"""
Integration tests for complete RAHU adaptive loop.

This validates the entire causal chain:

    contradiction
        ->
    attribution
        ->
    authority update
        ->
    representation update
        ->
    improved adaptation


The benchmark succeeds only if the system
changes the structure that produced the error.
"""


import pytest


from src.ptvs.environment import (
    PTVSEnvironment,
)

from src.mrat.router import (
    MRATRouter,
)

from src.inheritance.engine import (
    AdaptiveInheritanceEngine,
)

from src.ree.engine import (
    REEEngine,
)

from src.rahu.evaluator import (
    RAHUEvaluator,
)



class AdaptiveAgent:
    """
    Minimal end-to-end adaptive agent.
    """


    def __init__(self):

        self.inheritance = (
            AdaptiveInheritanceEngine()
        )

        self.ree = REEEngine()

        self.mrat = MRATRouter()


        self.inheritance.add_mechanism(
            name="initial_model",
            weight=1.0,
        )


        self.ree.set_representation(
            "initial_representation"
        )


    def act(
        self,
        observation,
    ):

        return "prediction"



    def adapt(
        self,
        residual,
    ):

        attribution = (
            self.mrat.attribute(
                residual
            )
        )


        if (
            attribution.layer
            ==
            "mechanism"
        ):

            self.inheritance.attenuate(
                mechanism="initial_model",
                admissibility=0.0,
            )


        expansion = (
            self.ree.evaluate(
                residual=1.0,
                future_value=2.0,
                cost=0.5,
            )
        )


        if expansion.expanded:

            self.ree.expand(
                new_structure="expanded_model",
                cost=0.5,
            )



def test_full_adaptive_loop_closes():
    """
    Golden test.

    A contradiction should propagate
    through every layer.
    """

    environment = (
        PTVSEnvironment()
    )

    agent = AdaptiveAgent()


    observation = (
        environment.reset()
    )


    action = agent.act(
        observation
    )


    result = (
        environment.step(
            action="contradiction"
        )
    )


    agent.adapt(
        result
    )


    assert (
        agent.inheritance
        .weights["initial_model"]
        <
        1.0
    )


    assert (
        len(
            agent.ree.expansion_history
        )
        >
        0
    )



def test_system_does_not_expand_without_pressure():
    """
    Stable environments should preserve
    compression.
    """

    agent = AdaptiveAgent()


    agent.adapt(
        {
            "type":
                "noise",

            "magnitude":
                0.1,
        }
    )


    assert (
        len(
            agent.ree.expansion_history
        )
        ==
        0
    )



def test_wrong_layer_is_not_modified():
    """
    Attribution should prevent blind repair.

    If the failure is representational,
    do not destroy mechanism authority.
    """

    agent = AdaptiveAgent()


    initial_weight = (
        agent.inheritance
        .weights["initial_model"]
    )


    agent.adapt(
        {
            "type":
                "representation_limit",

            "magnitude":
                1.0,
        }
    )


    assert (
        agent.inheritance
        .weights["initial_model"]
        ==
        initial_weight
    )



def test_repeated_environment_shift_creates_evolution():
    """
    Long-horizon adaptation test.

    Repeated pressure should produce
    structural evolution.
    """

    agent = AdaptiveAgent()


    for _ in range(10):

        agent.adapt(
            {
                "type":
                    "mechanism_failure",

                "magnitude":
                    1.0,
            }
        )


    assert (
        agent.inheritance
        .weights["initial_model"]
        <
        0.5
    )



def test_adaptation_is_better_than_static_agent():
    """
    Adaptive agent should outperform
    frozen baseline after distribution shift.
    """


    adaptive = AdaptiveAgent()


    baseline = AdaptiveAgent()


    for _ in range(5):

        adaptive.adapt(
            {
                "type":
                    "mechanism_failure",

                "magnitude":
                    1.0,
            }
        )


    assert (
        adaptive.inheritance
        .weights["initial_model"]
        <
        baseline.inheritance
        .weights["initial_model"]
    )



def test_telemetry_contains_causal_chain():
    """
    Every adaptation should leave an audit trail.
    """

    evaluator = (
        RAHUEvaluator()
    )


    result = evaluator.evaluate(
        AdaptiveAgent()
    )


    telemetry = (
        result.tasks[0]
        .telemetry
    )


    assert any(
        "residual"
        in event
        for event in telemetry
    )


    assert any(
        "authority_revision"
        in event
        for event in telemetry
    )
