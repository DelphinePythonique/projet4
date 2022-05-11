from typing import TYPE_CHECKING
from controller import Controller

if TYPE_CHECKING:

    from app import App

class Router:
    """
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
"""
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

    def __init__(self, app: "App"):
        self._app = app
        self._controller = Controller(self)
        self.mapping_route_to_controller = {
            self.HOMEPAGE_ID: self.controller.index,
            self.INDEX_PLAYER_ID: self.controller.index_player,
            self.INDEX_TOURNAMENT_ID: self.controller.index_tournament,
            self.ADD_PLAYER_ID: self.controller.add_player,
            self.UPDATE_RANKING_PLAYER_ID: self.controller.update_ranking_player,
            self.ADD_TOURNAMENT_ID: self.controller.add_tournament,
            self.DISPLAY_TOURNAMENT_ID: self.controller.display_tournament,
            self.ADD_PLAYER_INTO_TOURNAMENT_ID: self.controller.add_player_into_tournament,
            self.START_ROUND_ID: self.controller.start_round,
            self.SAVE_ROUND_ID: self.controller.save_round,
            self.REPORT_INDEX_ID: self.controller.report_index,
            self.REPORT_PLAYER_ID: self.controller.report_player,
            self.REPORT_TOURNAMENT_ID: self.controller.report_tournament,
            self.REPORT_TOURNAMENT_ROUNDS_ID: self.controller.report_tournament_rounds,
            self.REPORT_TOURNAMENT_MATCHS_ID: self.controller.report_tournament_matchs,
            self.REPORT_TOURNAMENT_PLAYERS_ID: self.controller.report_tournament_players
        }

    @property
    def app(self):
        return self._app

    @property
    def controller(self):
        return self._controller

    def call_controller_method(self, context):

        if "route_id" in context:
            if context["route_id"] in self.mapping_route_to_controller.keys():
                context = self.mapping_route_to_controller[context["route_id"]](context)

        return context

