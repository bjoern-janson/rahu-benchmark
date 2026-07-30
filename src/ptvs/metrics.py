"""
PTVS Metrics

Measurement functions for trajectory admissibility.

PTVS metrics describe empirical friction.
They do not explain causes or perform adaptation.

Primary metric:

    LBR (Latent Branch Ratio)

        inadmissible trajectories
    -------------------------------
        total trajectories

"""

from typing import List, Dict, Any


def compute_lbr(
    total_trajectories: int,
    invalid_trajectories: int,
) -> float:
    """
    Compute Latent Branch Ratio.

    LBR measures the proportion of evaluated
    trajectories that violate environmental
    admissibility constraints.

    Returns:
        float in [0,1]

    Interpretation:

        0.0:
            no detected constraint violations

        1.0:
            all evaluated trajectories violate
            constraints
    """

    if total_trajectories == 0:
        return 0.0

    return (
        invalid_trajectories /
        total_trajectories
    )


def compute_step_lbr(
    events: List[Dict[str, Any]],
) -> float:
    """
    Compute LBR directly from telemetry events.

    Expected event format:

    {
        "admissible": True/False
    }
    """

    if not events:
        return 0.0

    invalid = sum(
        1
        for event in events
        if not event.get("admissible", True)
    )

    return compute_lbr(
        total_trajectories=len(events),
        invalid_trajectories=invalid,
    )


def compute_violation_rate(
    events: List[Dict[str, Any]],
) -> Dict[str, float]:
    """
    Compute violation frequency by category.

    Useful for downstream MRAT analysis.

    Example:

        {
            "noise": 0.2,
            "mechanism_failure": 0.5,
            "representation_failure": 0.3
        }

    Note:
        This does NOT perform attribution.
        It only summarizes labels already
        supplied by the telemetry layer.
    """

    if not events:
        return {}

    counts = {}

    for event in events:
        if event.get("admissible", True):
            continue

        category = event.get(
            "violation_type",
            "unknown",
        )

        counts[category] = (
            counts.get(category, 0) + 1
        )

    total = sum(counts.values())

    if total == 0:
        return {}

    return {
        category: count / total
        for category, count in counts.items()
    }


def summarize_telemetry(
    events: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Produce PTVS measurement summary.

    Output is intended for MRAT ingestion.
    """

    invalid_count = sum(
        1
        for event in events
        if not event.get("admissible", True)
    )

    return {
        "trajectory_count": len(events),
        "invalid_count": invalid_count,
        "LBR": compute_step_lbr(events),
        "violation_distribution": (
            compute_violation_rate(events)
        ),
    }
