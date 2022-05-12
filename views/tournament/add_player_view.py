from typing import TYPE_CHECKING

from utils.input_utils import inputs_request
from views.player._utils import _format_display_players

if TYPE_CHECKING:
    from views.view import View


class TournamentAddPlayer:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            context.pop("tournament")
            context["route_id"] = self.router.DISPLAY_TOURNAMENT_ID
            if "players" in context:
                players = context["players"]
                context.pop("players")
                lines = ["Players"]
                player_lines, ids_list = _format_display_players(players)
                lines.extend(player_lines)
                lines.append("Enter players_id separated by ,")
                inputs_required = {
                    "players_select_ids": {
                        "question": lines,
                        "type": str,
                        "constraints": {'format': '^\\d+(,\\d+)*$'},
                    },
                }

                context = inputs_request(inputs_required, context_key="field", context=context)
                context["player_ids"] = context["field"]["players_select_ids"]
                context.pop("field")

                context["tournament"] = tournament
                context["tournament_id"] = tournament.identifier
        else:
            context["route_id"] = self.router.INDEX_TOURNAMENT_ID
        return context
