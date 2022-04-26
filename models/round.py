from datetime import datetime
import workflow.round.draft_state as draft_state
from models.match import Match
from models.player import Player
from workflow.round import start_state

DEFAULT_STATE = draft_state.DraftState()
RESULT_WINNER = 1
RESULT_LOSING = 0
RESULT_EQUALITY = 0.5


class Round:
    def __init__(self, name, tournament):
        self.name = name
        self.set_state(DEFAULT_STATE)
        self.tournament = tournament
        self.begin_date = None  # datetime.today()
        self.end_date = None
        self.matchs = []
        self.transition_to_start()

    def set_state(self, value):
        self._state = value
        self._state.round = self

    def get_state(self):
        return self._state

    def transition_to_draft(self):
        pass

    def transition_to_start(self):
        self._state.transition_to_start()

    def transition_to_stop(self):
        pass

    def do_the_paring_by_ranking(self):
        players = self.tournament.extract_tournament_player_sort_by_ranking()
        for i in range(0, len(players), 2):
            self.add_match(players[i], players[i + 1])

    def do_the_paring_by_total_rounds_result(self):
        players = self.tournament.extract_tournament_player_sort_by_result()
        print(players)
        """
        for i in range(0, len(players), 2):
            self.add_match(players[i], players[i + 1])
        """

    def add_match(self, player1, player2):
        self.matchs.append(Match(player1, player2).get_tuples())

    def display_matchs(self):
        for match in self.matchs:
            print(match)

    def who_is_players(self, match_index):
        return self.matchs[match_index][0][0], self.matchs[match_index][1][0]

    def set_match_equality(self, match_index):
        player1, player2 = self.who_is_players(match_index)
        self.matchs[match_index] = Match(player1, player2, RESULT_EQUALITY, RESULT_EQUALITY).get_tuples()

    def set_player_one_is_winner(self, match_index):
        player1, player2 = self.who_is_players(match_index)
        self.matchs[match_index] = Match(player1, player2, RESULT_WINNER, RESULT_LOSING).get_tuples()

    def set_player_two_is_winner(self, match_index):
        player1, player2 = self.who_is_players(match_index)
        self.matchs[match_index] = Match(player1, player2, RESULT_LOSING, RESULT_WINNER).get_tuples()

    def get_result_of_players(self):
        result_by_player = ()
        for match in self.matchs:
            result_by_player += tuple(match)
        return result_by_player

    def __repr__(self):
        return self.name
