import router
from utils.input_utils import inputs_request
from views import view
from views.tournament._utils import _format_matchs


class ReportTournamentMatchsView:
    def display(self, context):
        tournament = context["tournament"]
        lines = [
            f"Chess tournaments managment - Matchs of tournament {context['tournament'].name}",
        ]

        lines.extend([
            view.View.SEPARATOR,
            f"{router.Router.REPORT_INDEX_ID} - Menu Report",
            f"{router.Router.REPORT_TOURNAMENT_ID} - Report Tournament",
            view.View.SEPARATOR,
            "Enter the number of the action to be perform and press enter",
        ])
        for round_ in tournament.rounds:
            # if round_ == tournament.active_round:
            matchs_lines, match_ids = _format_matchs(round_)
            lines.extend(matchs_lines)

        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [router.Router.REPORT_INDEX_ID, router.Router.REPORT_TOURNAMENT_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        return context
