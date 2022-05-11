from models.player import Player
from models.tournament import Tournament
from router import Router


class App:

    def __init__(self):
        self.router = Router(self)
        self.players = []
        self.players_counter_for_identifier = 0
        self.tournaments = []
        self.tournaments_counter_for_identifier = 0
        Player.upload_players(self)
        Tournament.upload_tournaments(self)


if __name__ == "__main__":

    app = App()
    context = {'route_id': app.router.HOMEPAGE_ID}
    while 'route_id' in context:
        context = app.router.call_controller_method(context)
