import router

from utils.input_utils import inputs_request


class AppView():

    def index(self, context):
        lines = [
            "Chess tournaments managment",
            f"{router.Router.INDEX_PLAYER_ID} - Manage players",
            f"{router.Router.INDEX_TOURNAMENT_ID} - Manage tournaments",
            "Enter the number of the action to be perform and press enter",
        ]
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [router.Router.INDEX_PLAYER_ID, router.Router.INDEX_TOURNAMENT_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)

        if context["choice"]["menu"] == router.Router.INDEX_PLAYER_ID:
            context["route"] = router.Router.INDEX_PLAYER
        else:
            context["route"] = router.Router.INDEX_TOURNAMENT
        return context
