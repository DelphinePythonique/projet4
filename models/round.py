from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.tournament = tournament
        self.begin_date = None  # datetime.today()
        self.end_date = None

    @property
    def matchs(self):
        self._matchs = [match.tuple for match in Match.find_match_by_round(self)]
        return self._matchs

    def do_the_paring_by_ranking(self):
        players = self.tournament.extract_tournament_player_sort_by_ranking()
        for i in range(0, len(players), 2):
            self.add_match(players[i], players[i + 1])

    def do_the_paring_by_total_rounds_result(self):
        players = self.tournament.extract_tournament_player_sort_by_result()

        for i in range(0, len(players), 2):
            self.add_match(players[i][0], players[i + 1][0])

    def add_match(self, player1, player2):
        Match(self, player1, player2)

    def display_matchs(self):
        for match in self.matchs:
            print(match)

    def get_result_of_players(self):
        result_by_player = ()
        for match in self.matchs:
            result_by_player += tuple(match)
        return result_by_player

    def __repr__(self):
        return self.name
