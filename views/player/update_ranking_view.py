from utils.input_utils import inputs_request


class PlayerUpdateRankingView():
    def update_ranking_player(self, context):
        # with view asks for the new ranking of the player and return save message with index_player
        if "player" in context:
            print(context["player"])
        inputs_required = {
            "ranking": {"question": ["Enter ranking"], "type": int, "not_null": True, "constraints": {">=": 0}}
        }

        context = inputs_request(inputs_required, context_key="player_dict", context=context)
        context["player"].ranking = context["player_dict"]["ranking"]
        context["route"] = "index_players"
        return context
