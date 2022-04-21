import unittest

from models.player import Player


class TestModelPlayer(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        self.player = Player("Lemire", "Delphine", "01/01/1970", "feminine", None)

    def tearDown(self):
        self.player = None
        Player.players = []
        Player.players_counter_for_identifiant = 0

    def test_player_init(self):
        self.assertEqual(self.player.identifiant, 1, "identifiant is ok")
        self.assertEqual(self.player.surname, "Lemire", "surname is ok")
        self.assertEqual(len(Player.players), 1, "number  of player is ok")

    def test_player_set_ranking(self):
        self.player.set_ranking(10)
        self.assertEqual(self.player.ranking, 10, "ranking is ok")
