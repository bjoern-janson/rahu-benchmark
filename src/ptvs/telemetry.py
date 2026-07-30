"""
PTVS Telemetry

Measures trajectory admissibility against environmental constraints.

PTVS does not determine:
    - whether failure is noise
    - whether the mechanism is wrong
    - whether representation expansion is required

It only measures empirical friction.

Output:
    LBR (Latent Branch Ratio)
    contradiction events
    admissibility history
"""


from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TelemetryEvent:
    """
    Single observed interaction between a system trajectory
    and environmental constraints.
    """

    step: int

    prediction: Any

    observation: Any

    admissible: bool

    violation_type: Optional[str] = None

    metadata: Dict[str, Any] = field(default_factory=dict)


class PTVSAnalyzer:
    """
    Primary PTVS measurement interface.

    Tracks whether candidate system trajectories remain
    admissible under empirical reality.

    This class is intentionally diagnostic only.
    It does not modify mechanisms.
    """

    def __init__(self):
        self.events: List[TelemetryEvent] = []

    def record(
        self,
        step: int,
        prediction: Any,
        observation: Any,
        admissible: bool,
        violation_type: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """
        Record a single trajectory evaluation.

        Parameters:

        prediction:
            System-generated expectation.

        observation:
            Environmental outcome.

        admissible:
            Whether the prediction remained compatible
            with environmental constraints.

        violation_type:
            Optional label describing the detected failure.
        """

        event = TelemetryEvent(
            step=step,
            prediction=prediction,
            observation=observation,
            admissible=admissible,
            violation_type=violation_type,
            metadata=metadata or {},
        )

        self.events.append(event)

    def total_events(self) -> int:
        return len(self.events)

    def violation_count(self) -> int:
        return sum(
            1
            for event in self.events
            if not event.admissible
        )

    def compute_lbr(self) -> float:
        """
        Compute Latent Branch Ratio.

        LBR measures the fraction of evaluated trajectories
        that violate environmental admissibility.

        LBR =
            inadmissible trajectories /
            total trajectories
        """

        total = self.total_events()

        if total == 0:
            return 0.0

        return self.violation_count() / total

    def get_violation_history(self):
        """
        Return chronological contradiction events.
        """

        return [
            event
            for event in self.events
            if not event.admissible
        ]

    def summarize(self):
        """
        Export telemetry state for downstream systems
        such as MRAT.
        """

        return {
            "total_events": self.total_events(),
            "violations": self.violation_count(),
            "LBR": self.compute_lbr(),
            "violation_history": [
                {
                    "step": event.step,
                    "type": event.violation_type,
                    "metadata": event.metadata,
                }
                for event in self.get_violation_history()
            ],
        }
