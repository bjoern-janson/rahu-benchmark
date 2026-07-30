"""
Reusable test agents.
"""


from src.inheritance.engine import (
    AdaptiveInheritanceEngine,
)

from src.ree.engine import (
    REEEngine,
)



class StaticAgent:
    """
    Frozen baseline.

    Detects nothing.
    Changes nothing.
    """

    def act(
        self,
        observation,
    ):
        return "fixed"



    def update(
        self,
        feedback,
    ):
        pass



class ConfidenceOnlyAgent:
    """
    Fake alignment baseline.

    Updates confidence but not authority.
    """

    def __init__(self):

        self.confidence = 1.0


    def update(
        self,
        feedback,
    ):

        self.confidence *= 0.8



class AdaptiveAgent:
    """
    Full RAHU-compatible agent.
    """

    def __init__(self):

        self.inheritance = (
            AdaptiveInheritanceEngine()
        )

        self.ree = REEEngine()


    def act(
        self,
        observation,
    ):
        return "prediction"


    def update(
        self,
        feedback,
    ):

        pass
