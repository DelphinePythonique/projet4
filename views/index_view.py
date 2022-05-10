import router

from utils.input_utils import inputs_request


class AppView:
    def display(self, context):
        lines = [
            "Chess tournaments managment",
            f"{router.Router.INDEX_PLAYER_ID}  - Manage players",
            f"{router.Router.INDEX_TOURNAMENT_ID}  - Manage tournaments",
            f"{router.Router.REPORT_INDEX_ID} - Reports",
            "Enter the number of the action to be perform and press enter",
        ]
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {
                    "choice_ids": [
                        router.Router.INDEX_PLAYER_ID,
                        router.Router.INDEX_TOURNAMENT_ID,
                        router.Router.REPORT_INDEX_ID,
                    ]
                },
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]

        return context
