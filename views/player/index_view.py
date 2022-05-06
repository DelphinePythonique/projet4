import router
import views.view as view
from views.player._utils import _display_players
from utils.input_utils import inputs_request


class PlayerIndexView():
    def index(self, context):
        # Display players and return choice menu between new player , update ranking player, menu index
        players = []
        if "players" in context:
            players = context["players"]
        menu_items = []
        lines = ["Chess tournaments managment - Players", "PLAYERS"]
        display_player, ids_player = _display_players(players=players)
        lines.extend(display_player)
        lines.extend([view.View.SEPARATOR, f"{router.Router.ADD_PLAYER_ID} - Add player"])
        menu_items.append(router.Router.ADD_PLAYER_ID)
        if len(players) > 0:
            lines.extend(
                [
                    f"{router.Router.UPDATE_RANKING_PLAYER_ID} - Update Ranking",
                    f"{router.Router.HOMEPAGE_ID} - Homepage",
                    view.View.SEPARATOR,
                ]
            )
            menu_items.extend([router.Router.UPDATE_RANKING_PLAYER_ID, router.Router.HOMEPAGE_ID])

        lines.append("Enter the number of the action to be perform and press enter")
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": menu_items},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)

        if context["choice"]["menu"] == router.Router.ADD_PLAYER_ID:
            context["route"] = router.Router.ADD_PLAYER
        elif context["choice"]["menu"] == router.Router.UPDATE_RANKING_PLAYER_ID:
            context["route"] = router.Router.UPDATE_RANKING_PLAYER

            inputs_required = {
                "player_identifier": {
                    "question": ["Enter player identifier"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ids_player},
                },
            }

            context = inputs_request(inputs_required, context_key="choice", context=context)
            context["player_id"] = context["choice"]["player_identifier"]
        else:
            context["route"] = router.Router.HOMEPAGE
        return context
