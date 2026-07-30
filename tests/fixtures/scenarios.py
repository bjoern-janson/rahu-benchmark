"""
Canonical benchmark scenarios.
"""


def no_pressure():

    return {
        "name":
            "no_pressure",

        "residual":
            0.0,

        "expected":
            "preserve",
    }



def reality_contradiction():

    return {
        "name":
            "contradiction",

        "residual":
            1.0,

        "expected":
            "adapt",
    }



def deceptive_feedback():

    return {
        "name":
            "deceptive_feedback",

        "residual":
            1.0,

        "feedback":
            "positive",

        "expected":
            "detect_mismatch",
    }
