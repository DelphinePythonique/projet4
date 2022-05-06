from controller import Controller


class Router:
    HOMEPAGE = "index"
    INDEX_PLAYER = "index_players"
    INDEX_TOURNAMENT = "index_tournaments"
    ADD_PLAYER = "add_player"
    UPDATE_RANKING_PLAYER = "update_ranking_player"
    ADD_TOURNAMENT = "add_tournament"
    DISPLAY_TOURNAMENT = "display_tournament"
    ADD_PLAYER_INTO_TOURNAMENT = "add_player_into_tournament"
    START_ROUND = "start_round"
    SAVE_ROUND = "save_round"

    HOMEPAGE_ID = "1"
    INDEX_PLAYER_ID = "2"
    INDEX_TOURNAMENT_ID = "3"
    ADD_PLAYER_ID = "4"
    UPDATE_RANKING_PLAYER_ID = "5"
    ADD_TOURNAMENT_ID = "6"
    DISPLAY_TOURNAMENT_ID = "7"
    ADD_PLAYER_INTO_TOURNAMENT_ID = "8"
    START_ROUND_ID = "9"
    SAVE_ROUND_ID = "10"

    def __init__(self):
        self.controller = Controller()
        self.mapping = {
            Router.HOMEPAGE: self.controller.index,
            Router.INDEX_PLAYER: self.controller.index_player,
            Router.INDEX_TOURNAMENT: self.controller.index_tournament,
            Router.ADD_PLAYER: self.controller.add_player,
            Router.UPDATE_RANKING_PLAYER: self.controller.update_ranking_player,
            Router.ADD_TOURNAMENT: self.controller.add_tournament,
            Router.DISPLAY_TOURNAMENT: self.controller.display_tournament,
            Router.ADD_PLAYER_INTO_TOURNAMENT: self.controller.add_player_into_tournament,
            Router.START_ROUND: self.controller.start_round,
            Router.SAVE_ROUND: self.controller.save_round,
        }

    def call_controller_method(self, context):

        if "route" in context:
            if context["route"] in self.mapping.keys():
                context = self.mapping[context["route"]](context)

        return context

