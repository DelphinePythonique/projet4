import router
from utils.input_utils import inputs_request


class ReportTournamentPlayersView:
    def display(self, context):
        lines = [
            "Chess tournaments managment",
            f"{router.Router.HOMEPAGE_ID} - Homepage",
            "Enter the number of the action to be perform and press enter",
        ]
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [router.Router.HOMEPAGE_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        return context
