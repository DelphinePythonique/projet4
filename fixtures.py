""" Do list of players"""
from models.match import Match
from models.player import Player
from models.tournament import Tournament

player1 = Player("joueurA-100", "Delphine", "01/01/1970", "feminine", 100)
player2 = Player("joueurB-100", "Jean", "01/01/1971", "masculine", 100)
player3 = Player("joueurA-30", "Remi", "01/01/1971", "masculine", 30)
player4 = Player("joueurA-20", "Delphine", "01/01/1970", "feminine", 20)
player5 = Player("joueurA-50", "Jean", "01/01/1971", "masculine", 50)
player6 = Player("joueurB-30", "Remi", "01/01/1971", "masculine", 30)
player7 = Player("joueurC-100", "Delphine", "01/01/1970", "feminine", 100)
player8 = Player("joueurD-100", "Jean", "01/01/1971", "masculine", 100)
player9 = Player("joueurC-30", "Remi", "01/01/1971", "masculine", 30)
player10 = Player("joueurB-20", "Delphine", "01/01/1970", "feminine", 20)
player11 = Player("joueurB-50", "Jean", "01/01/1971", "masculine", 50)
player12 = Player("joueurD-30", "Remi", "01/01/1971", "masculine", 30)

tournament = Tournament("tournament of 20/05/2022", "Rouen", "20/05/2022", "20/05/2022", "blitz")
tournament.add_player(player1)
tournament.add_player(player2)
tournament.add_player(player3)
tournament.add_player(player4)
tournament.add_player(player5)
tournament.add_player(player6)
tournament.add_player(player7)
tournament.add_player(player8)

