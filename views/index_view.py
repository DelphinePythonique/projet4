from typing import TYPE_CHECKING

from utils.input_utils import inputs_request

if TYPE_CHECKING:
    from view import View


class AppView:
    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        lines = [
            "Chess tournaments managment",
            f"{self.router.INDEX_PLAYER_ID}  - Manage players",
            f"{self.router.INDEX_TOURNAMENT_ID}  - Manage tournaments",
            f"{self.router.REPORT_INDEX_ID} - Reports",
            "Enter the number of the action to be perform and press enter",
        ]
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {
                    "choice_ids": [
                        self.router.INDEX_PLAYER_ID,
                        self.router.INDEX_TOURNAMENT_ID,
                        self.router.REPORT_INDEX_ID,
                    ]
                },
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        context.pop("choice")

        return context
