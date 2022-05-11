from typing import TYPE_CHECKING

from utils.input_utils import inputs_request
from views.tournament._utils import _format_display_tournaments

if TYPE_CHECKING:
    from views.view import View


class ReportTournamentView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        ids_tournaments = []
        items_menu = {
            self.router.REPORT_TOURNAMENT_ROUNDS_ID: "Report rounds of tournament",
            self.router.REPORT_TOURNAMENT_MATCHS_ID: "Report matchs of tournament ",
            self.router.REPORT_TOURNAMENT_PLAYERS_ID: "Report players of tournament",
            self.router.REPORT_INDEX_ID: "Report menu",
        }
        lines = ["Chess tournaments managment "]

        if "tournaments" in context:
            tournaments = context["tournaments"]
            lines_tournaments, ids_tournaments = _format_display_tournaments(tournaments)
            lines.extend(lines_tournaments)
        lines.append(self.view.SEPARATOR)
        for key, value in items_menu.items():
            lines.append(f"{key} - {value}")

        lines.extend(
            [
                self.view.SEPARATOR,
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
            self.router.REPORT_TOURNAMENT_ROUNDS_ID,
            self.router.REPORT_TOURNAMENT_MATCHS_ID,
            self.router.REPORT_TOURNAMENT_PLAYERS_ID,
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
        if context["route_id"] == self.router.REPORT_TOURNAMENT_PLAYERS_ID:
            inputs_required = {
                "sorted_by": {
                    "question": ["What sort order do you want; 1: by alphapetic surname, 2: by ranking?"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ["1", "2"]},
                },
            }
            context = inputs_request(inputs_required, context_key="question", context=context)
            if context['question']['sorted_by'] == "1":
                context['sorted_by'] = 'surname'
            else:
                context['sorted_by'] = 'ranking'
        return context
