# Copyright 2024-TODAY Francesco Apruzzese <cescoap@gmail.com>
# License GPL-3.0 or later (https://www.gnu.org/licenses/gpl-3.0).

BASE_EVENTS = {
    "__END__army": {
        "description": "You lost control of the army. You have been ousted from the highest military office!",
    },
    "__END__environment": {
        "description": "You did not take into account the environment. Nature takes back everything that is its own!",
    },
    "__END__faith": {
        "description": "People have lost faith. Evil will rule the world!",
    },
    "__END__happiness": {
        "description": "People, now too sad, have left their belongings to seek happiness elsewhere!",
    },
    "__END__health": {
        "description": "The worst epidemics have hit your people. Health is now an old memory!",
    },
    "__END__politic": {
        "description": "You have become too corrupt. It's time for you to pay for your choices!",
    },
    "__END__science": {
        "description": "Trust in science has been lost. We have gone too far!",
    },
    "__END__wealth": {
        "description": "Too much money in the hands of too few people. Poverty has taken over!",
    },
    "__WIN__": {"description": "You are all that people need. Thank you for your great work!"},
}


EVENTS = {
    "influencer_no_vax": {
        "description": "A famous influencer has declared that she does not believe in vaccines. "
        "People are beginning to be suspicious.",
        "options": {
            "option1": {
                "description": "Ignore her",
                "effects": {
                    "science": -10,
                    "politic": -5,
                },
            },
            "option2": {
                "description": "Respond on social",
                "effects": {
                    "health": +10,
                    "politic": +5,
                },
            },
            "option3": {
                "description": "Kill her",
                "effects": {
                    "happiness": -50,
                    "army": +50,
                    "science": +10,
                    "politic": -5,
                },
            },
        },
        "repeatable": False,
    },
    "bike_demand": {
        "description": "People are calling for more bike lanes so they can safely ride their bikes",
        "options": {
            "option1": {
                "description": "Create new bike lines",
                "effects": {
                    "health": +10,
                    "happiness": +10,
                    "wealth": -20,
                    "politic": +5,
                    "environment": +20,
                },
            },
            "option2": {
                "description": "Ignore them",
                "effects": {
                    "health": -10,
                    "happiness": -10,
                    "politic": -5,
                },
            },
        },
        "repeatable": True,
    },
    "immigration_fear": {
        "description": "The newspaper headlines are talking about an immigration alert. "
        "People are starting to get scared",
        "options": {
            "option1": {
                "description": "Keep your borders open",
                "effects": {
                    "health": -5,
                    "happiness": -5,
                    "wealth": -10,
                    "politic": -5,
                    "faith": +10,
                },
            },
            "option2": {
                "description": "Close the borders",
                "effects": {
                    "happiness": +5,
                    "politic": +10,
                    "faith": -10,
                },
            },
        },
        "repeatable": True,
    },
}
