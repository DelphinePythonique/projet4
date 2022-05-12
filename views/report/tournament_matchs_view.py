from typing import TYPE_CHECKING


from utils.input_utils import inputs_request

from views.tournament._utils import _format_matchs

if TYPE_CHECKING:
    from views.view import View


class ReportTournamentMatchsView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        tournament = context["tournament"]
        context.pop("tournament")
        lines = [
            f"Chess tournaments managment - Matchs of tournament {context['tournament'].name}",
        ]

        lines.extend([
            self.view.SEPARATOR,
            f"{self.router.REPORT_INDEX_ID} - Menu Report",
            f"{self.router.REPORT_TOURNAMENT_ID} - Report Tournament",
            self.view.SEPARATOR,
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
                "constraints": {"choice_ids": [self.router.REPORT_INDEX_ID, self.router.REPORT_TOURNAMENT_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        context.pop("choice")
        return context
