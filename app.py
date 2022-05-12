from tinydb import TinyDB

from models.player import Player
from models.tournament import Tournament
from router import Router


class App:

    def __init__(self, db_name="db2.json"):
        self.router = Router(self)
        self.players = []
        self.players_counter_for_identifier = 0
        self.tournaments = []
        self.tournaments_counter_for_identifier = 0
        self._db = TinyDB(db_name)

        Player.upload_players(self)
        Tournament.upload_tournaments(self)

    def charge_fixtures(self):
        from models.player import Player
        from models.tournament import Tournament

        player1 = Player(self, "joueurA-100", "Delphine", "01/01/1970", "feminine", 100)
        player2 = Player(self, "joueurB-100", "Jean", "01/01/1971", "masculine", 100)
        player3 = Player(self, "joueurA-30", "Remi", "01/01/1971", "masculine", 30)
        player4 = Player(self, "joueurA-20", "Delphine", "01/01/1970", "feminine", 20)
        player5 = Player(self, "joueurA-50", "Jean", "01/01/1971", "masculine", 50)
        player6 = Player(self, "joueurB-30", "Remi", "01/01/1971", "masculine", 30)
        player7 = Player(self, "joueurC-100", "Delphine", "01/01/1970", "feminine", 100)
        player8 = Player(self, "joueurD-100", "Jean", "01/01/1971", "masculine", 100)

        for player in self.players:
            player.save()

        tournament = Tournament(self, "tournament of 20/05/2022", "Rouen", "20/05/2022", "20/05/2022", "blitz")
        tournament.save()
        tournament.add_player(player1)
        tournament.add_player(player2)
        tournament.add_player(player3)
        tournament.add_player(player4)
        tournament.add_player(player5)
        tournament.add_player(player6)
        tournament.add_player(player7)
        tournament.add_player(player8)
        tournament.save()

    @property
    def player_table(self):
        return self._db.table("players")

    @property
    def tournament_table(self):
        return self._db.table("tournaments")

    @property
    def db(self):
        return self._db


if __name__ == "__main__":

    app = App("db_verif.json")
    # app.charge_fixtures()
    context = {'route_id': app.router.HOMEPAGE_ID}
    while 'route_id' in context:
        context = app.router.call_controller_method(context)
