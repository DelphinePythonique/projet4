from datetime import datetime
from typing import TYPE_CHECKING

from utils.input_utils import inputs_request

if TYPE_CHECKING:
    from views.view import View


class PlayerAddView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        # with view asks for the entry of the information of the new player and return save message with index_player
        inputs_required = {
            "surname": {
                "question": ["Enter surname"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "first_name": {
                "question": ["Enter first_name"],
                "type": str,
                "not_null": True,
                "constraints": {"max_nb_car": 50},
            },
            "date_of_birth": {"question": ["Enter date_of_birth as DD/MM/YYYY"], "type": datetime},
            "gender": {
                "question": ["Enter gender (m for masculine, f for feminine, o for other)"],
                "type": str,
                "constraints": {"max_nb_car": 1, "format": "^[f|m|o]$"},
            },
            "ranking": {"question": ["Enter ranking"], "type": int, "not_null": True, "constraints": {">=": 0}},
        }

        print("Enter player informations")
        context = inputs_request(inputs_required, context_key="player", context=context)
        context["route_id"] = self.router.INDEX_PLAYER_ID
        return context
