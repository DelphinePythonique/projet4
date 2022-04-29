class Match:
    """
    composition([player1,score1],[player2,score2])
    """
    STATE_START = 'start'
    STATE_STOP = "stop"
    RESULT_WINNER = 1
    RESULT_LOSING = 0
    RESULT_EQUALITY = 0.5
    matchs = []

    @staticmethod
    def find_match_by_tuple(round, match_tuple):
        match_found = [match for match in Match.matchs if match.round == round and match.tuple == match_tuple][0]
        return match_found

    @staticmethod
    def find_match_by_round(round):
        match_found = [match for match in Match.matchs if match.round == round ]
        return match_found

    def __init__(self, round, player1, player2, result_player1=0, result_player2=0):
        self.round = round
        self.player1 = player1
        self.player2 = player2
        self.result_player1 = result_player1
        self.result_player2 = result_player2
        Match.matchs.append(self)

    @property
    def state(self):
        if self.result_player1 + self.result_player2 == 0:
            self._state = Match.STATE_START
        else:
            self._state = Match.STATE_STOP

        return self._state

    @property
    def tuple(self):
        return [(self.player1, self.result_player1), (self.player2, self.result_player2)]

    def who_is_players(self):
        return self.player1, self.player2

    def set_match_equality(self):
        self.result_player1 = Match.RESULT_EQUALITY
        self.result_player2 = Match.RESULT_EQUALITY

    def set_player_one_is_winner(self):
        self.result_player1 = Match.RESULT_WINNER
        self.result_player2 = Match.RESULT_LOSING

    def set_player_two_is_winner(self):
        self.result_player1 = Match.RESULT_LOSING
        self.result_player2 = Match.RESULT_WINNER
