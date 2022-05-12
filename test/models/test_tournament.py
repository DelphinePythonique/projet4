import os
import unittest

from app import App
from models.player import Player
from models.tournament import Tournament


class TestModelTournament(unittest.TestCase):
    BDD_FILE = 'db_test.json'

    def setUp(self):
        self.tearDown()
        self.app = App(TestModelTournament.BDD_FILE)
        self.tournament = Tournament(self.app, "tournament of 20/05/2022", "Rouen", "20/05/2022", "20/05/2022", "blitz")
        self.player1 = Player(self.app, "Lemire", "Delphine", "01/01/1970", "feminine", 150)
        self.player2 = Player(self.app, "Dubois", "Jean", "01/01/1971", "masculine", 1)
        self.player3 = Player(self.app, "Lamy", "Remi", "01/01/1971", "masculine", 2)
        self.player4 = Player(self.app, "Dupond", "Delphine", "01/01/1970", "feminine", 300)
        self.player5 = Player(self.app, "Dupont", "Jean", "01/01/1971", "masculine", 50)
        self.player6 = Player(self.app, "Dubois", "Remi", "01/01/1971", "masculine", 20)
        self.player7 = Player(self.app, "Deschamps", "Remi", "01/01/1971", "masculine", 11)
        self.player8 = Player(self.app, "Lulu", "Remi", "01/01/1971", "masculine", 2)

    def tearDown(self):
        self.tournament = None
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.player5 = None
        self.player6 = None
        self.player7 = None
        self.player8 = None
        if os.path.exists(TestModelTournament.BDD_FILE):
            os.remove(TestModelTournament.BDD_FILE)

    def test_tournament_init(self):
        self.assertEqual(self.tournament.identifier, 1, "identifier is ok")
        self.assertEqual(self.tournament.name, "tournament of 20/05/2022", "name is ok")
        self.assertEqual(self.tournament.number_of_round, 4, "number of round is ok")
        self.assertEqual(len(self.app.tournaments), 1, "number  of tournaments is ok")

    def test_tournament_set_tournament_set_time_control(self):
        self.tournament.time_control = 'bullet'
        self.assertEqual(self.tournament.time_control, "bullet", "time control is ok")
        self.tournament.time_control = 'bad_time_control'
        self.assertEqual(self.tournament.time_control, Tournament.DEFAULT_TIME_CONTROL, "time control is ok")

    def test_tournament_add_player(self):

        self.tournament.add_player(self.player1)
        self.assertEqual(self.tournament.players[0], 1, "add player by objet player is ok")
        self.tournament.add_player(self.player2.identifier)
        self.assertEqual(self.tournament.players[1], 2, "add player by player's idenfifiant is ok")
        self.tournament.add_player(100)
        self.assertTrue(100 not in self.tournament.players)

    def test_tournament_generate_round(self):
        self.tournament.generate_round()
        self.assertEqual(len(self.tournament.rounds), 4, "generate rounds is ok")

    def test_tournament_check_state(self):
        self.assertEqual(self.tournament.state, Tournament.STATE_DRAFT)
        self.tournament.add_player(self.player1.identifier)
        self.tournament.add_player(self.player2.identifier)
        self.tournament.add_player(self.player3.identifier)
        self.tournament.add_player(self.player4.identifier)
        self.tournament.add_player(self.player5.identifier)
        self.tournament.add_player(self.player6.identifier)
        self.tournament.add_player(self.player7.identifier)
        self.assertEqual(self.tournament.state, Tournament.STATE_DRAFT)
        self.tournament.start_round()
        self.assertEqual(self.tournament.state, Tournament.STATE_DRAFT)
        self.tournament.add_player(self.player8.identifier)
        self.assertEqual(self.tournament.state, Tournament.STATE_READY)
        self.tournament.start_round()
        self.assertEqual(self.tournament.state, Tournament.STATE_IN_PROGRESS)
