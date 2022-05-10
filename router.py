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
    REPORT_INDEX = "report_index"
    REPORT_PLAYER = "report_player"
    REPORT_TOURNAMENT = "report_tournament"
    REPORT_TOURNAMENT_ROUNDS = "report_tournament_rounds"
    REPORT_TOURNAMENT_MATCHS = "report_tournament_matchs"
    REPORT_TOURNAMENT_PLAYERS = "report_tournament_players"

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
    REPORT_INDEX_ID = "11"
    REPORT_PLAYER_ID = "12"
    REPORT_TOURNAMENT_ID = "13"
    REPORT_TOURNAMENT_ROUNDS_ID = "14"
    REPORT_TOURNAMENT_MATCHS_ID = "15"
    REPORT_TOURNAMENT_PLAYERS_ID = "16"

    def __init__(self, app):
        self.controller = Controller(app)
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
            Router.REPORT_INDEX: self.controller.report_index,
            Router.REPORT_PLAYER: self.controller.report_player,
            Router.REPORT_TOURNAMENT: self.controller.report_tournament,
            Router.REPORT_TOURNAMENT_ROUNDS: self.controller.report_tournament_rounds,
            Router.REPORT_TOURNAMENT_MATCHS: self.controller.report_tournament_matchs,
            Router.REPORT_TOURNAMENT_PLAYERS: self.controller.report_tournament_players
        }

    def call_controller_method(self, context):

        if "route" in context:
            if context["route"] in self.mapping.keys():
                context = self.mapping[context["route"]](context)

        return context

