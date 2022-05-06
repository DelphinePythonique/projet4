from models.player import Player
from models.tournament import Tournament
from router import Router


class App:

    def __init__(self):
        self.router = Router()
        Player.upload_players()
        Tournament.upload_tournaments()


if __name__ == "__main__":

    app = App()
    context = {'route': Router.HOMEPAGE}
    while 'route' in context:
        context = app.router.call_controller_method(context)
