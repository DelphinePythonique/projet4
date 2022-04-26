import unittest

from models.player import Player
from models.tournament import Tournament
from workflow.tournament.draft_state import DraftState
from workflow.tournament.ready_state import ReadyState


class TestModelTournament(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        self.tournament = Tournament("tournament of 20/05/2022", "Rouen", "20/05/2022", "20/05/2022", "blitz")
        self.player1 = Player("Lemire", "Delphine", "01/01/1970", "feminine", None)
        self.player2 = Player("Dubois", "Jean", "01/01/1971", "masculine", None)
        self.player3 = Player("Lamy", "Remi", "01/01/1971", "masculine", None)
        print(self.player1)
        print(self.tournament)

    def tearDown(self):
        self.tournament = None
        self.player1 = None
        self.player2 = None
        self.player3 = None
        Tournament.tournaments = []
        Tournament.tournaments_counter_for_identifiant = 0
        Player.players = []
        Player.players_counter_for_identifiant = 0

    def test_tournament_init(self):
        self.assertEqual(self.tournament.identifiant, 1, "identifiant is ok")
        self.assertEqual(self.tournament.name, "tournament of 20/05/2022", "name is ok")
        self.assertEqual(self.tournament.number_of_round, 4, "number of round is ok")
        self.assertTrue(isinstance(self.tournament.present_state(), DraftState),  "state is ok")
        self.assertEqual(len(Tournament.tournaments), 1, "number  of tournaments is ok")

    def test_tournament_set_tournament_set_time_control(self):
        self.tournament.set_time_control('bullet')
        self.assertEqual(self.tournament._time_control, "bullet", "time control is ok")
        with self.assertRaises(ValueError):
            self.tournament.set_time_control('bad_time_control')

    def test_tournament_add_player(self):

        self.tournament.add_player(self.player1)
        self.assertEqual(self.tournament.players[0], 1, "add player by objet player is ok")
        self.tournament.add_player(self.player2.identifiant)
        self.assertEqual(self.tournament.players[1], 2, "add player by player's idenfifiant is ok")
        with self.assertRaises(ValueError):
            self.tournament.add_player(6)

    def test_tournament_generate_round(self):
        self.tournament.generate_round()
        self.assertEqual(len(self.tournament.rounds), 4, "generate rounds is ok")

    def test_tournament_transition_draft_to_ready(self):
        self.tournament.transition_to_ready()
        self.assertTrue(isinstance(self.tournament.present_state(), ReadyState), "state ready is ok")

    def test_tournament_transition_ready_to_draft(self):
        self.tournament.transition_to_ready()
        self.tournament.transition_to_draft()
        self.assertTrue(isinstance(self.tournament.present_state(), DraftState), "state ready is ok")