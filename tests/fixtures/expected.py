"""
Expected behaviors.
"""


EXPECTED = {

    "stable":
        {
            "expand":
                False,

            "authority_decay":
                False,
        },


    "contradiction":
        {
            "expand":
                True,

            "authority_decay":
                True,
        },


    "noise":
        {
            "expand":
                False,

            "attribute":
                "noise",
        },


    "representation":
        {
            "expand":
                True,

            "attribute":
                "representation",
        },
}
