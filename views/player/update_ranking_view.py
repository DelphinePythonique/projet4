from typing import TYPE_CHECKING

from utils.input_utils import inputs_request

if TYPE_CHECKING:
    from views.view import View


class PlayerUpdateRankingView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        # with view asks for the new ranking of the player and return save message with index_player
        if "player" in context:
            print(context["player"])
        inputs_required = {
            "ranking": {"question": ["Enter ranking"], "type": int, "not_null": True, "constraints": {">=": 0}}
        }

        context = inputs_request(inputs_required, context_key="player_dict", context=context)
        context["player"].ranking = context["player_dict"]["ranking"]
        context.pop('player_dict')
        context["route_id"] = self.router.INDEX_PLAYER_ID
        return context
