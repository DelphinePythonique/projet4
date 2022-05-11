from typing import TYPE_CHECKING

from utils.input_utils import inputs_request

if TYPE_CHECKING:
    from views.view import View


class ReportTournamentRoundsView:

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
        lines = [
            f"Chess tournaments managment - Rounds of tournament {context['tournament']}",
        ]

        lines.extend([
            f"{self.router.REPORT_INDEX_ID} - Menu Report",
            f"{self.router.REPORT_TOURNAMENT_ID} - Report Tournament",
            "Enter the number of the action to be perform and press enter",
        ])
        for round_ in tournament.rounds:
            # if round_ == tournament.active_round:

            lines.append(f"Round {round_.name} {round_.state}")
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
        return context
