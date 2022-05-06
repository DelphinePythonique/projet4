from views.index_view import AppView
import router

from utils.system_utils import clear_screen
from views.player.add_view import PlayerAddView
from views.player.index_view import PlayerIndexView
from views.player.update_ranking_view import PlayerUpdateRankingView
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
        mapping = {
            router.Router.HOMEPAGE: AppView().index,
            router.Router.INDEX_PLAYER: PlayerIndexView().index,
            router.Router.ADD_PLAYER: PlayerAddView().add,
            router.Router.ADD_TOURNAMENT: TournamentAddView().add,
            router.Router.UPDATE_RANKING_PLAYER: PlayerUpdateRankingView().update_ranking_player,
            router.Router.INDEX_TOURNAMENT: TournamentIndexView().index,
            router.Router.DISPLAY_TOURNAMENT: TournamentDisplayView().display,
            router.Router.ADD_PLAYER_INTO_TOURNAMENT: TournamentAddPlayer().add_player_into_tournament,
        }
        if "view" in context:
            if context["view"] in mapping:
                context = mapping[context["view"]](context)
        else:
            context = self.index(context)
        return context
