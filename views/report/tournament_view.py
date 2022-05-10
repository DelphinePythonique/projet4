import router
from utils.input_utils import inputs_request
from views import view
from views.tournament._utils import _format_display_tournaments


class ReportTournamentView:
    def display(self, context):
        ids_tournaments = []
        items_menu = {
            router.Router.REPORT_TOURNAMENT_ROUNDS_ID: "Report rounds of tournament",
            router.Router.REPORT_TOURNAMENT_MATCHS_ID: "Report matchs of tournament ",
            router.Router.REPORT_TOURNAMENT_PLAYERS_ID: "Report players of tournament",
            router.Router.REPORT_INDEX_ID: "Report menu",
        }
        lines = ["Chess tournaments managment "]

        if "tournaments" in context:
            tournaments = context["tournaments"]
            lines_tournaments, ids_tournaments = _format_display_tournaments(tournaments)
            lines.extend(lines_tournaments)
        lines.append(view.View.SEPARATOR)
        for key, value in items_menu.items():
            lines.append(f"{key} - {value}")

        lines.extend(
            [
                view.View.SEPARATOR,
                "Enter the number of the action to be perform and press enter",
            ]
        )

        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": items_menu.keys()},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        if context["route_id"] in (
            router.Router.REPORT_TOURNAMENT_ROUNDS_ID,
            router.Router.REPORT_TOURNAMENT_MATCHS_ID,
            router.Router.REPORT_TOURNAMENT_PLAYERS_ID,
        ):
            inputs_required = {
                "tournament_id": {
                    "question": ["From which tournaments do you want to display the rounds, enter the tournament ID?"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ids_tournaments},
                },
            }

            context = inputs_request(inputs_required, context_key="question", context=context)
            context['tournament_id'] = context['question']['tournament_id']
        return context
