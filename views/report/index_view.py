from typing import TYPE_CHECKING

from utils.input_utils import inputs_request

if TYPE_CHECKING:
    from views.view import View


class ReportIndexView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        items_menu = {
            self.router.REPORT_PLAYER_ID: "Report players",
            self.router.REPORT_TOURNAMENT_ID: "Report tournaments",
            self.router.HOMEPAGE_ID: "Homepage",
        }
        lines = ["Chess tournaments managment"]
        for key, value in items_menu.items():
            lines.append(f"{key} - {value}")

        lines.append("Enter the number of the action to be perform and press enter")

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
        context.pop("choice")
        if context["route_id"] == self.router.REPORT_PLAYER_ID:
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
            context.pop("question")
        return context
