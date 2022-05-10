import router
from utils.input_utils import inputs_request
from views.player._utils import _format_display_players


class TournamentAddPlayer:
    def display(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            context["route_id"] = router.Router.DISPLAY_TOURNAMENT_ID
            if "players" in context:
                players = context["players"]

                lines = ["Players"]
                player_lines, ids_list = _format_display_players(players)
                lines.extend(player_lines)
                lines.append("Enter players_id separated by ,")
                inputs_required = {
                    "players_select_ids": {
                        "question": lines,
                        "type": str,
                        "constraints": {"format": "^\d+(,\d+)*$"},
                    },
                }

                context = inputs_request(inputs_required, context_key="field", context=context)
                context["player_ids"] = context["field"]["players_select_ids"]

                context["tournament"] = tournament
                context["tournament_id"] = tournament.identifier
        else:
            context["route_id"] = router.Router.INDEX_TOURNAMENT_ID
        return context
