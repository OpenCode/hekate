# Copyright 2024-TODAY Francesco Apruzzese <cescoap@gmail.com>
# License GPL-3.0 or later (https://www.gnu.org/licenses/gpl-3.0).

import webbrowser
from random import choice, randint

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

from consts.base import BUILD, CARD_IMAGES_URL, HOMEPAGE_URL, PARAMETERS, VERSION
from consts.event import BASE_EVENTS, EVENTS


class Hekate(MDApp):
    """
    A class representing the main application for the Hekate game.

    The Hekate game is a card-based decision-making game. The player is presented with a series
    of events (represented as cards) and must choose an option for each event. Each option has
    effects on the game's parameters, and the game ends when any parameter drops to zero or below.

    Attributes:
        parameters: A dictionary of game parameters with random initial values.
        id_card: The id of the current card being displayed.
        extracted_cards: A list of ids of cards that have already been drawn.

    Methods:
        build(): Sets up the game layout and initial parameter values.
        start(): Initiates the game by clearing the current widgets and moving to the next card.
        end(reason): Ends the game due to a loss, clears the current widgets, and displays the end card.
        win(): Ends the game with a win, clears the current widgets and displays the win card.
        option_press(instance): Handles the event when an option button is pressed.
        next_card(): Clears the current widgets and initializes the next card from the pool of possible events.
        visit_website(): Opens the specified homepage URL in the default webbrowser.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Init random parameters
        self.parameters = {k: randint(20, 70) for k in PARAMETERS}
        # Init generic data
        self.id_card = "__START__"
        self.extracted_cards = []

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        builder = Builder.load_file("layout/game.kv")
        # Assign dinamically randon values to parameters
        for parameter in PARAMETERS:
            builder.ids[f"{parameter}_progress"].value = self.parameters[parameter]
        # Adapt version from data
        version = builder.ids.version_label.text
        version = version.replace("__VERSION__", str(VERSION))
        version = version.replace("__BUILD__", str(BUILD))
        builder.ids.version_label.text = version
        return builder

    def start(self):
        """
        Initiates the game by clearing the current widgets and moving to the next card (the first one).
        """
        self.root.ids.options_buttons.clear_widgets()
        self.next_card()

    def end(self, reason):
        """
        Ends the game due to a loss, clears the current widgets, and displays the end card with
        the corresponding reason.
        Also, replaces the standard icon with the defeat icon.

        Args:
            reason: The reason for the game end, used to determine which end card and defeat icon to display.
        """
        self.root.ids.options_buttons.clear_widgets()
        self.id_card = "__END__"
        self.root.ids.card_image.source = f"assets/base/end_{reason}.jpg"
        self.root.ids.card_description.text = BASE_EVENTS[f"__END__{reason}"]["description"]
        # Replace standard icon with defeat one
        self.root.ids[f"{reason}_icon"].icon = PARAMETERS[reason]["defeat_icon"]

    def win(self):
        """
        Ends the game with a win, clears the current widgets and displays the win card.
        """
        self.root.ids.options_buttons.clear_widgets()
        self.id_card = "__WIN__"
        self.root.ids.card_image.source = "assets/base/win.jpg"
        self.root.ids.card_description.text = BASE_EVENTS["__WIN__"]["description"]

    def option_press(self, instance):
        """
        Handles the event when an option button is pressed.
        It retrieves the selected option and associated event data.
        Then, it applies the effects of the selected option to the relevant parameters and updates
        the corresponding progress bar.
        If any parameter drops to zero or below, it triggers the end of the game.
        Otherwise, it proceeds to the next card.

        Args:
            instance: The instance of the button that was pressed.
        """
        option = instance.id.replace("_button", "")
        id_event = self.id_card
        event_data = EVENTS[id_event]
        end_game_reason = ""
        for effect, value in event_data["options"][option]["effects"].items():
            self.parameters[effect] += value
            self.root.ids[f"{effect}_progress"].value += value
            if self.parameters[effect] <= 0:
                end_game_reason = effect
                break
        if end_game_reason:
            self.end(end_game_reason)
        else:
            self.next_card()

    def next_card(self):
        """
        Clears the current widgets and initializes the next card from the pool of possible events.
        If no possible events are left, triggers the win condition.
        Otherwise, randomly selects an event, updates the card description and image,
        and creates a new button for each option associated with the event.
        Each button is bound to the option_press function and added to the options_buttons widget.
        """
        self.root.ids.options_buttons.clear_widgets()
        possible_events = [ev for ev in list(EVENTS.keys()) if ev not in self.extracted_cards]
        if not possible_events:
            self.win()
            return
        id_event = choice(possible_events)
        self.id_card = id_event
        self.extracted_cards.append(id_event)
        event_data = EVENTS[id_event]
        self.root.ids.card_description.text = event_data["description"]
        self.root.ids.card_image.source = f"assets/cards/{id_event}.jpg"
        for option, option_data in event_data["options"].items():
            button = MDRaisedButton(
                id=f"{option}_button",
                text=option_data["description"],
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size_hint=(1, 1),
            )
            button.bind(on_press=self.option_press)
            self.root.ids.options_buttons.add_widget(button)

    def visit_website(self, site):
        """
        Opens the specified website URL in the default webbrowser.
        The website opened depends on the 'site' argument passed.

        Args:
            site (str): A string that specifies the website to visit.
                        'home' opens the home page URL
                        'card_images' opens the card images URL.
        """
        if site == "home":
            webbrowser.open(HOMEPAGE_URL)
        elif site == "card_images":
            webbrowser.open(CARD_IMAGES_URL)


if __name__ == "__main__":
    Hekate().run()
