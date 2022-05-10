from models.match import Match
from models.player import Player
from models.tournament import Tournament
from views.view import View
import router


class Controller:
    def __init__(self, app):
        self.app = app
        self.view = View()

    def index(self, context):
        # Display menu #1 and return choice menu between player index or Tournament index

        context = self.view.render_view(context)
        return context

    def index_player(self, context):
        # Display players and return choice menu between new player , update ranking player, menu index
        context["players"] = Player.list_of_players_by_alphabetic_sort(self.app.players)

        context = self.view.render_view(context)
        return context

    def add_player(self, context):
        # with view asks for the entry of the information of the new player and return save message with index_player

        context = self.view.render_view(context)
        if "player" in context:
            player = Player.dict_to_object(self.app, context["player"])
            player.save()
            context["player"] = player
        return context

    def update_ranking_player(self, context):
        # with view asks for the new ranking of the player and return save message with index_player
        if "choice" in context:
            if "player_identifier" in context["choice"]:
                context["player"] = Player.find_player_by_identifier(self.app, int(context["choice"]["player_identifier"]))
            else:
                context = {}
                self.index_player(context)
        context = self.view.render_view(context)
        if "player" in context:
            player = context["player"]
            player.save()

        return context

    def index_tournament(self, context):
        # Display tournaments and return choice menu between new tournament, display tournament, menu index
        context["tournaments"] = self.app.tournaments

        context = self.view.render_view(context)
        return context

    def add_tournament(self, context):
        # with view asks for the entry of the information of the new tournament and return save message with index tournament

        context = self.view.render_view(context)
        if "tournament" in context:
            tournament = Tournament.dict_to_object(self.app, context["tournament"])
            tournament.save()
            context["tournament"] = tournament
        return context

    def display_tournament(self, context):
        # display tournament, return menu choice between start_round, add player, save result match
        if "tournament_id" in context:
            context["tournament"] = Tournament.find_tournament_by_identifier(self.app, int(context["tournament_id"]))
            context["tournament_players"] = []
            for player_id in context["tournament"].players:
                context["tournament_players"].append(Player.find_player_by_identifier(self.app, player_id))

        context = self.view.render_view(context)
        return context

    def add_player_into_tournament(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            players = [
                player
                for player in Player.list_of_players_by_alphabetic_sort(self.app.players)
                if player.identifier not in tournament.players
            ]
            context["players"] = players

            context = self.view.render_view(context)
            if "tournament" in context:
                tournament = context["tournament"]
                if "player_ids" in context:
                    players_ids_list = context["player_ids"].split(",")
                    for player_id in players_ids_list:
                        player_id = player_id.strip()
                        tournament.add_player(int(player_id))
                        tournament.save()
        else:
            context["route"] = router.Router.HOMEPAGE
        return context

    def start_round(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            tournament.start_round()
            tournament.save()
        context["route"] = router.Router.DISPLAY_TOURNAMENT
        return context

    def save_round(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            if "match" and "match_result" in context:
                match = Match.find_match_by_tuple(tournament.active_round, context["match"])
                if context["match_result"] == "1":
                    match.set_player_one_is_winner()
                elif context["match_result"] == "2":
                    match.set_player_two_is_winner()
                else:
                    match.set_match_equality()
            tournament.save()
        context["route"] = router.Router.DISPLAY_TOURNAMENT
        return context

    def report_index(self, context):
        context = self.view.render_view(context)
        return context

    def report_player(self, context):
        if context["sorted_by"] == 'surname':
            players = Player.list_of_players_by_alphabetic_sort(self.app.players)
        else:
            players = Player.list_of_players_by_ranking_sort(self.app.players)
        context["players"] = players
        context = self.view.render_view(context)
        return context

    def report_tournament(self, context):
        context["tournaments"] = self.app.tournaments
        context = self.view.render_view(context)
        return context

    def report_tournament_rounds(self, context):
        tournament_id = context["tournament_id"]
        context["tournament"] = Tournament.find_tournament_by_identifier(self.app, int(tournament_id))
        context = self.view.render_view(context)
        return context

    def report_tournament_matchs(self, context):
        tournament_id = context["tournament_id"]
        context["tournament"] = Tournament.find_tournament_by_identifier(self.app, int(tournament_id))
        context = self.view.render_view(context)
        return context

    def report_tournament_players(self, context):
        tournament_id = context["tournament_id"]
        context["tournament"] = Tournament.find_tournament_by_identifier(self.app, int(tournament_id))
        context["tournament_players"] = []
        for player_id in context["tournament"].players:
            context["tournament_players"].append(Player.find_player_by_identifier(self.app, player_id))
        context = self.view.render_view(context)
        return context
