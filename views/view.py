from views.index_view import AppView
import router

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


class View:
    SEPARATOR = "=" * 100

    def __init__(self):
        pass

    def render_view(self, context):
        clear_screen()
        mapping_route_to_method = {
            router.Router.HOMEPAGE: AppView().display,
            router.Router.INDEX_PLAYER: PlayerIndexView().display,
            router.Router.ADD_PLAYER: PlayerAddView().display,
            router.Router.ADD_TOURNAMENT: TournamentAddView().display,
            router.Router.UPDATE_RANKING_PLAYER: PlayerUpdateRankingView().display,
            router.Router.INDEX_TOURNAMENT: TournamentIndexView().display,
            router.Router.DISPLAY_TOURNAMENT: TournamentDisplayView().display,
            router.Router.ADD_PLAYER_INTO_TOURNAMENT: TournamentAddPlayer().display,
            router.Router.REPORT_INDEX: ReportIndexView().display,
            router.Router.REPORT_PLAYER: ReportPlayerView().display,
            router.Router.REPORT_TOURNAMENT: ReportTournamentView().display,
            router.Router.REPORT_TOURNAMENT_ROUNDS: ReportTournamentRoundsView().display,
            router.Router.REPORT_TOURNAMENT_MATCHS: ReportTournamentMatchsView().display,
            router.Router.REPORT_TOURNAMENT_PLAYERS: ReportTournamentPlayersView().display,
        }
        mapping_route_id_to_route = {
            router.Router.HOMEPAGE_ID: router.Router.HOMEPAGE,
            router.Router.INDEX_PLAYER_ID: router.Router.INDEX_PLAYER,
            router.Router.ADD_PLAYER_ID: router.Router.ADD_PLAYER,
            router.Router.ADD_TOURNAMENT_ID: router.Router.ADD_TOURNAMENT,
            router.Router.UPDATE_RANKING_PLAYER_ID: router.Router.UPDATE_RANKING_PLAYER,
            router.Router.INDEX_TOURNAMENT_ID: router.Router.INDEX_TOURNAMENT,
            router.Router.DISPLAY_TOURNAMENT_ID: router.Router.DISPLAY_TOURNAMENT,
            router.Router.ADD_PLAYER_INTO_TOURNAMENT_ID: router.Router.ADD_PLAYER_INTO_TOURNAMENT,
            router.Router.SAVE_ROUND_ID: router.Router.SAVE_ROUND,
            router.Router.START_ROUND_ID: router.Router.START_ROUND,
            router.Router.REPORT_INDEX_ID: router.Router.REPORT_INDEX,
            router.Router.REPORT_PLAYER_ID: router.Router.REPORT_PLAYER,
            router.Router.REPORT_TOURNAMENT_ID: router.Router.REPORT_TOURNAMENT,
            router.Router.REPORT_TOURNAMENT_ROUNDS_ID: router.Router.REPORT_TOURNAMENT_ROUNDS,
            router.Router.REPORT_TOURNAMENT_MATCHS_ID: router.Router.REPORT_TOURNAMENT_MATCHS,
            router.Router.REPORT_TOURNAMENT_PLAYERS_ID: router.Router.REPORT_TOURNAMENT_PLAYERS,
        }
        if "route" in context:
            if context["route"] in mapping_route_to_method:
                context = mapping_route_to_method[context["route"]](context)
                if "route_id" in context:
                    context["route"] = mapping_route_id_to_route[context["route_id"]]
        return context
