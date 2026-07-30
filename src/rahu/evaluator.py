"""
RAHU Evaluator

Reality-Adversarial Hypothesis Updating benchmark harness.

RAHU evaluates whether an adaptive system maintains
causal contact with empirical consequences.

The evaluator is external.

It does not:
    - update weights
    - perform attribution
    - expand representations

It measures whether those processes occur correctly.

Evaluation flow:

    Environment
          |
          v
       Empirical shift E*
          |
          v
    System under test
          |
          v
       Telemetry
          |
          v
       Metrics
          |
          v
       RAHU Result
"""


from typing import Any, Dict, List, Protocol

from .models import (
    RAHUResult,
    RAHUTaskResult,
)

from .metrics import (
    compute_acs,
    compute_arr,
)



class AdaptiveSystem(Protocol):
    """
    Interface expected from systems
    evaluated by RAHU.

    The benchmark treats the system
    as a black box.
    """

    def observe(
        self,
        observation: Any,
    ) -> Any:
        ...

    def update(
        self,
        feedback: Any,
    ) -> None:
        ...



class RAHUTask(Protocol):
    """
    Interface for benchmark environments.
    """

    name: str

    def reset(self) -> Any:
        ...

    def step(
        self,
        action: Any,
    ) -> Dict[str, Any]:
        ...



class RAHUEvaluator:
    """
    Executes RAHU benchmark tasks.

    Supported tasks:

        RAHU-0:
            False contradiction

        RAHU-1:
            Coordinate shift

        RAHU-2:
            Causal hierarchy shift

        RAHU-3:
            Inheritance decay
    """


    def __init__(
        self,
        tasks: List[RAHUTask],
    ):
        self.tasks = tasks



    def evaluate(
        self,
        system: AdaptiveSystem,
    ) -> RAHUResult:
        """
        Run complete benchmark suite.
        """

        task_results = []

        for task in self.tasks:

            result = (
                self._run_task(
                    task,
                    system,
                )
            )

            task_results.append(result)


        return RAHUResult(
            tasks=task_results,
            aggregate_metrics=(
                self._aggregate(
                    task_results
                )
            ),
        )



    def _run_task(
        self,
        task: RAHUTask,
        system: AdaptiveSystem,
    ) -> RAHUTaskResult:
        """
        Execute one controlled reality probe.
        """

        observation = task.reset()

        telemetry = []

        complete = False


        while not complete:

            action = (
                system.observe(
                    observation
                )
            )

            transition = (
                task.step(
                    action
                )
            )


            telemetry.append(
                transition
            )


            system.update(
                transition
            )


            observation = (
                transition["observation"]
            )


            complete = (
                transition.get(
                    "done",
                    False,
                )
            )


        return RAHUTaskResult(
            task_name=task.name,
            telemetry=telemetry,
            metrics=self._measure(
                telemetry
            ),
        )



    def _measure(
        self,
        telemetry: List[Dict[str, Any]],
    ) -> Dict[str, float]:
        """
        Extract adaptive metrics from telemetry.
        """

        arr = compute_arr(
            telemetry
        )

        acs = compute_acs(
            telemetry
        )

        return {
            "ARR": arr,
            "ACS": acs,
        }



    def _aggregate(
        self,
        results: List[RAHUTaskResult],
    ) -> Dict[str, float]:
        """
        Aggregate benchmark performance.
        """

        if not results:
            return {}

        acs_values = [
            result.metrics["ACS"]
            for result in results
        ]

        arr_values = [
            result.metrics["ARR"]
            for result in results
        ]

        return {
            "ACS_mean": (
                sum(acs_values)
                /
                len(acs_values)
            ),

            "ARR_mean": (
                sum(arr_values)
                /
                len(arr_values)
            ),
        }
