from datetime import datetime
from models.match import Match


class Round:
    STATE_DRAFT = "draft"
    STATE_START = "start"
    STATE_STOP = "stop"
    RANKING_PARING_METHOD = 'ranking'
    RESULT_PARING_METHOD = 'result'

    def __init__(self, name, tournament, number):
        self.name = name
        self.number = number
        self.tournament = tournament
        self.begin_date = None  # datetime.today()
        self.end_date = None

    @property
    def state(self):
        if len(self.matchs) == 0:
            self._state = Round.STATE_DRAFT
        elif len(self.matchs) > 0:
            matchs_start = [match for match in  Match.find_match_by_round(self) if match.state == Match.STATE_START]
            if len(matchs_start) > 0:
                self._state = Round.STATE_START
            else:
                self._state = Round.STATE_STOP

        return self._state

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

    def start(self, paring_method):
        if self.state == Round.STATE_DRAFT:
            if paring_method == Round.RANKING_PARING_METHOD:
                self.do_the_paring_by_ranking()
            elif paring_method == Round.RESULT_PARING_METHOD:
                self.do_the_paring_by_total_rounds_result()

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
