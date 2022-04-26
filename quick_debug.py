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
tournament.generate_round()
for round in tournament.rounds:
    print(round)

print("list of player sort by ranking, alphabetic")
for player in tournament.extract_tournament_player_sort_by_ranking():
    print(f"id:{player.identifier}({player.surname}): ranking:{player.ranking}")

tournament.rounds[0].do_the_paring_by_ranking()

print("round #0 - Matchs")
for match in tournament.rounds[0].matchs:
    print(f"player #1:{match[0][0].identifier} / player #2:{match[1][0].identifier} ")

match1 = Match.find_match_by_tuple(round=tournament.rounds[0], match_tuple=tournament.rounds[0].matchs[0])
match1.set_match_equality()
match2 = Match.find_match_by_tuple(round=tournament.rounds[0], match_tuple=tournament.rounds[0].matchs[1])
match2.set_player_one_is_winner()
match3 = Match.find_match_by_tuple(round=tournament.rounds[0], match_tuple=tournament.rounds[0].matchs[2])
match3.set_player_two_is_winner()
match4 = Match.find_match_by_tuple(round=tournament.rounds[0], match_tuple=tournament.rounds[0].matchs[3])
match4.set_player_one_is_winner()

print("list of player sort by result last matchs")
for player, result in tournament.extract_tournament_player_sort_by_result():
    print(f"id:{player.identifier}({player.surname}): result:{result}")
print("round #1 - Matchs")
tournament.rounds[1].do_the_paring_by_total_rounds_result()
for match in tournament.rounds[1].matchs:
    print(f"player #1:{match[0][0].identifier} / player #2:{match[1][0].identifier} ")


match1 = Match.find_match_by_tuple(round=tournament.rounds[1], match_tuple=tournament.rounds[1].matchs[0])
match1.set_match_equality()
match2 = Match.find_match_by_tuple(round=tournament.rounds[1], match_tuple=tournament.rounds[1].matchs[1])
match2.set_player_one_is_winner()
match3 = Match.find_match_by_tuple(round=tournament.rounds[1], match_tuple=tournament.rounds[1].matchs[2])
match3.set_player_two_is_winner()
match4 = Match.find_match_by_tuple(round=tournament.rounds[1], match_tuple=tournament.rounds[1].matchs[3])
match4.set_player_one_is_winner()

print("list of player sort by result last matchs")
for player, result in tournament.extract_tournament_player_sort_by_result():
    print(f"id:{player.identifier}({player.surname}): result:{result}")

print("round #2 - Matchs")
tournament.rounds[2].do_the_paring_by_total_rounds_result()
for match in tournament.rounds[2].matchs:
    print(f"player #1:{match[0][0].identifier} / player #2:{match[1][0].identifier} ")
