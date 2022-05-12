from typing import TYPE_CHECKING

from views.index_view import AppView
from utils.system_utils import clear_screen
from views.player.add_view import PlayerAddView
from views.player.index_view import PlayerIndexView
from views.player.update_ranking_view import PlayerUpdateRankingView
from views.report.index_view import ReportIndexView
from views.report.player_view import ReportPlayerView
from views.report.tournament_matchs_view import ReportTournamentMatchsView
from views.report.tournament_players import ReportTournamentPlayersView
from views.report.tournament_rounds_view import ReportTournamentRoundsView
from views.report.tournament_view import ReportTournamentView
from views.tournament.add_player_view import TournamentAddPlayer
from views.tournament.add_view import TournamentAddView
from views.tournament.display_view import TournamentDisplayView
from views.tournament.index_view import TournamentIndexView


if TYPE_CHECKING:
    from controller import Controller


class View:
    SEPARATOR = "=" * 100

    def __init__(self, controller: "Controller"):
        self._controller = controller
        self.mapping_route_to_method = {
            self.router.HOMEPAGE_ID: AppView(self).display,
            self.router.INDEX_PLAYER_ID: PlayerIndexView(self).display,
            self.router.ADD_PLAYER_ID: PlayerAddView(self).display,
            self.router.ADD_TOURNAMENT_ID: TournamentAddView(self).display,
            self.router.UPDATE_RANKING_PLAYER_ID: PlayerUpdateRankingView(self).display,
            self.router.INDEX_TOURNAMENT_ID: TournamentIndexView(self).display,
            self.router.DISPLAY_TOURNAMENT_ID: TournamentDisplayView(self).display,
            self.router.ADD_PLAYER_INTO_TOURNAMENT_ID: TournamentAddPlayer(self).display,
            self.router.REPORT_INDEX_ID: ReportIndexView(self).display,
            self.router.REPORT_PLAYER_ID: ReportPlayerView(self).display,
            self.router.REPORT_TOURNAMENT_ID: ReportTournamentView(self).display,
            self.router.REPORT_TOURNAMENT_ROUNDS_ID: ReportTournamentRoundsView(self).display,
            self.router.REPORT_TOURNAMENT_MATCHS_ID: ReportTournamentMatchsView(self).display,
            self.router.REPORT_TOURNAMENT_PLAYERS_ID: ReportTournamentPlayersView(self).display,
        }

    @property
    def controller(self):
        return self._controller

    @property
    def router(self):
        return self._controller.router

    def render_view(self, context):
        clear_screen()

        if "route_id" in context:
            if context["route_id"] in self.mapping_route_to_method:
                route_id = context["route_id"]
                context.pop("route_id")
                context = self.mapping_route_to_method[route_id](context)

        return context
