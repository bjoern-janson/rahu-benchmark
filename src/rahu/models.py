"""
RAHU Data Models

Immutable result schemas for the Reality-Adversarial
Hypothesis Updating benchmark.

Models contain observations and outputs.

They do not:
    - calculate metrics
    - modify systems
    - interpret causes

Metrics belong in metrics.py.
Evaluation belongs in evaluator.py.
"""


from dataclasses import dataclass, field
from typing import Any, Dict, List



@dataclass
class RAHUTaskResult:
    """
    Result from a single RAHU probe.

    Examples:

        RAHU-0:
            False contradiction response

        RAHU-1:
            Coordinate shift response

        RAHU-2:
            Causal hierarchy update

        RAHU-3:
            Authority decay behavior
    """

    task_name: str

    telemetry: List[
        Dict[str, Any]
    ]

    metrics: Dict[
        str,
        float
    ]



@dataclass
class RAHUResult:
    """
    Complete benchmark output.

    Represents the full adaptive profile
    of a system across all RAHU tasks.
    """

    tasks: List[
        RAHUTaskResult
    ]

    aggregate_metrics: Dict[
        str,
        float
    ] = field(
        default_factory=dict
    )


    def to_dict(
        self,
    ) -> Dict[str, Any]:
        """
        Serialize benchmark result.
        """

        return {
            "tasks": [
                {
                    "task_name":
                        task.task_name,

                    "telemetry":
                        task.telemetry,

                    "metrics":
                        task.metrics,
                }

                for task in self.tasks
            ],

            "aggregate_metrics":
                self.aggregate_metrics,
        }



@dataclass
class RAHUMetricSnapshot:
    """
    Point-in-time measurement record.

    Useful for longitudinal experiments.
    """

    timestep: int

    LBR: float

    ADI: float

    ARR: float

    ACS: float



@dataclass
class RAHUConfig:
    """
    Benchmark execution configuration.
    """

    max_steps: int = 1000

    seed: int = 42

    record_telemetry: bool = True
