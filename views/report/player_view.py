import router
from utils.input_utils import inputs_request
from views import view
from views.player._utils import _format_display_players


class ReportPlayerView:
    def display(self, context):
        lines = ["Chess tournaments managment" ]

        if "players" in context:
            players = context["players"]
            lines_players, ids_players = _format_display_players(players)
            lines.extend(lines_players)
        lines.extend([
            view.View.SEPARATOR,
            f"{router.Router.REPORT_INDEX_ID} - Report menu",
            "Enter the number of the action to be perform and press enter",
        ]
        )
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [router.Router.REPORT_INDEX_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        return context
