import os
import unittest

from tinydb import where

from app import App
from models.player import Player


class TestModelPlayer(unittest.TestCase):
    BDD_FILE = 'db_test.json'

    def setUp(self):
        self.tearDown()
        self.app = App(TestModelPlayer.BDD_FILE)
        self.player = Player(self.app, "Lemire", "Delphine", "01/01/1970", "feminine", 450)
        self.player1 = Player(self.app, "Piotre", "Romain", "01/01/1973", "feminine", 250)
        self.player2 = Player(self.app, "Biche", "Roberte", "01/01/1980", "feminine", 300)

    def tearDown(self):
        self.player = None
        if os.path.exists(TestModelPlayer.BDD_FILE):
            os.remove(TestModelPlayer.BDD_FILE)

    def test_player_init(self):

        self.assertEqual(self.player.identifier, 1, "identifier is ok")
        self.assertEqual(self.player.surname, "Lemire", "surname is ok")
        self.assertEqual(len(self.app.players), 3, "number  of player is ok")

    def test_player_set_ranking(self):
        self.player.ranking = 10
        self.assertEqual(self.player.ranking, 10, "ranking is ok")

    def test_save(self):
        players = self.app.player_table.search(where('surname') == 'Lemire')
        self.assertEqual(len(players), 0)
        self.player.save()
        players = self.app.player_table.search(where('surname') == 'Lemire')
        self.assertEqual(len(players), 1)
        self.player.ranking = 100
        self.player.save()
        players = self.app.player_table.search(where('surname') == 'Lemire')
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0]['ranking'], 100)

    def test_find_player(self):
        player = Player.find_player_by_identifier(self.app, self.player.identifier)
        self.assertEqual(player.identifier, 1)

    def test_list_of_players_by_alphabetic_sort(self):
        players = Player.list_of_players_by_alphabetic_sort(self.app.players)
        self.assertEqual(players[0].identifier, 3)
        self.assertEqual(players[1].identifier, 1)
        self.assertEqual(players[2].identifier, 2)

    def test_list_of_players_by_ranking_sort(self):
        players = Player.list_of_players_by_ranking_sort(self.app.players)
        self.assertEqual(players[0].identifier, 2)
        self.assertEqual(players[1].identifier, 3)
        self.assertEqual(players[2].identifier, 1)

    def test_dict_to_player(self):
        dict = {'surname': 'Pick', 'first_name': 'nick', 'date_of_birth': '16/05/1999', 'gender': 'm', 'ranking': 150}
        player = Player.dict_to_object(self.app, dict)
        self.assertEqual(player.surname, 'Pick')
