from os.path import exists

from tinydb import TinyDB

from models.player import Player
from models.tournament import Tournament
from router import Router
#import fixtures


class App:

    def __init__(self):
        self.router = Router()
        Player.upload_players()
        Tournament.upload_tournaments()


if __name__ == "__main__":

    app = App()
    context = {'route': 'homepage'}
    while 'route' in context:
        context = app.router.call_controller_method(context)
