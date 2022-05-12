from typing import TYPE_CHECKING

from utils.input_utils import inputs_request
from views.tournament._utils import _format_display_tournaments

if TYPE_CHECKING:
    from views.view import View


class TournamentIndexView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        tournaments = []
        menu_items = [self.router.ADD_TOURNAMENT_ID]
        if "tournaments" in context:
            tournaments = context["tournaments"]
            context.pop('tournaments')
        # Display tournaments and return choice menu between new tournament, display tournament, menu index
        # Display players and return choice menu between new player , update ranking player, menu index

        lines = ["Chess tournaments managment - Tournament", self.view.SEPARATOR, "Tournaments"]
        tournament_lines, ids_tournaments = _format_display_tournaments(tournaments)
        lines.extend(tournament_lines)
        lines.extend([self.view.SEPARATOR, f"{self.router.ADD_TOURNAMENT_ID} - Add Tournament"])
        if len(tournaments) > 0:
            lines.extend(
                [
                    f"{self.router.DISPLAY_TOURNAMENT_ID} - Display tournament",
                    f"{self.router.HOMEPAGE_ID} - Homepage",
                    self.view.SEPARATOR,

                ]
            )
            menu_items.extend([self.router.DISPLAY_TOURNAMENT_ID, self.router.HOMEPAGE_ID])

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
        context.pop("choice")
        if context["route_id"] == self.router.DISPLAY_TOURNAMENT_ID:
            inputs_required = {
                "tournament_identifier": {
                    "question": ["Enter tournament identifier"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ids_tournaments},
                },
            }

            context = inputs_request(inputs_required, context_key="choice", context=context)
            context["tournament_id"] = context["choice"]["tournament_identifier"]
            context.pop('choice')

        return context
