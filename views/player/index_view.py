from typing import TYPE_CHECKING

from views.player._utils import _format_display_players
from utils.input_utils import inputs_request
if TYPE_CHECKING:
    from views.view import View


class PlayerIndexView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        # Display players and return choice menu between new player , update ranking player, menu index
        players = []
        if "players" in context:
            players = context["players"]
        menu_items = []
        lines = ["Chess tournaments managment - Players", "PLAYERS"]
        display_player, ids_player = _format_display_players(players=players)
        lines.extend(display_player)
        lines.extend([self.view.SEPARATOR, f"{self.router.ADD_PLAYER_ID} - Add player"])
        menu_items.append(self.router.ADD_PLAYER_ID)
        if len(players) > 0:
            lines.extend(
                [
                    f"{self.router.UPDATE_RANKING_PLAYER_ID} - Update Ranking",
                    f"{self.router.HOMEPAGE_ID} - Homepage",
                    self.view.SEPARATOR,
                ]
            )
            menu_items.extend([self.router.UPDATE_RANKING_PLAYER_ID, self.router.HOMEPAGE_ID])

        lines.append("Enter the number of the action to be perform and press enter")
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": menu_items},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        context.pop('choice')
        if context["route_id"] == self.router.UPDATE_RANKING_PLAYER_ID:
            inputs_required = {
                "player_identifier": {
                    "question": ["Enter player identifier"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ids_player},
                },
            }

            context = inputs_request(inputs_required, context_key="choice", context=context)
            context["player_id"] = context["choice"]["player_identifier"]
            context.pop("choice")
        return context
