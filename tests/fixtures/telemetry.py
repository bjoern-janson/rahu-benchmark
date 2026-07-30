"""
Synthetic telemetry traces.
"""


def successful_adaptation_trace():

    return [

        {
            "residual": 1.0,

            "authority_revision":
                1.0,

            "confidence_revision":
                0.5,

            "authority_changed":
                True,
        }

    ]



def failed_adaptation_trace():

    return [

        {
            "residual": 1.0,

            "authority_revision":
                0.0,

            "confidence_revision":
                1.0,

            "authority_changed":
                False,
        }

    ]
