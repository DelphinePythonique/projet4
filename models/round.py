from math import ceil

from models.match import Match


class Round:
    STATE_DRAFT = "draft"
    STATE_START = "start"
    STATE_STOP = "stop"
    RANKING_PARING_METHOD = 'ranking'
    RESULT_PARING_METHOD = 'result'

    def __init__(self, name, tournament, number, begin_date=None, end_date=None):
        self.name = name
        self.number = number
        self.tournament = tournament
        self.begin_date = begin_date  # datetime.today()
        self.end_date = end_date

    @property
    def state(self):
        state = Round.STATE_DRAFT
        if len(self.matchs) == 0:
            state = Round.STATE_DRAFT
        elif len(self.matchs) > 0:
            matchs_start = [match for match in Match.find_match_by_round(self) if match.state == Match.STATE_START]
            if len(matchs_start) > 0:
                state = Round.STATE_START
            else:
                state = Round.STATE_STOP

        return state

    @property
    def matchs(self):
        matchs = [match.tuple for match in Match.find_match_by_round(self)]
        return matchs

    def __repr__(self):
        return self.name

    def do_the_paring_by_ranking(self):
        players = self.tournament.extract_tournament_player_sort_by_ranking()
        half_number_player = ceil(len(players) / 2)
        for i in range(0, half_number_player):
            self.add_match(players[i], players[i + half_number_player])

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

    def serialized_round(self):

        serialized_round = {
            'name': self.name,
            'number': self.number,
            'begin_date': self.begin_date,
            'end_date': self.end_date,
            'matchs': []
        }
        for match_tuple in self.matchs:
            match = Match.find_match_by_tuple(self, match_tuple)
            serialized_round['matchs'].append(match.serialized_match_tuple())
        return serialized_round
