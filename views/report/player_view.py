from typing import TYPE_CHECKING


from utils.input_utils import inputs_request
from views.player._utils import _format_display_players

if TYPE_CHECKING:
    from views.view import View

class ReportPlayerView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router


    def display(self, context):
        lines = ["Chess tournaments managment"]

        if "players" in context:
            players = context["players"]
            lines_players, ids_players = _format_display_players(players)
            lines.extend(lines_players)
        lines.extend([
            self.view.SEPARATOR,
            f"{self.router.REPORT_INDEX_ID} - Report menu",
            "Enter the number of the action to be perform and press enter",
        ]
        )
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [self.router.REPORT_INDEX_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        return context
