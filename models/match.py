class Match:
    """
    composition([player1,score1],[player2,score2])
    """

    def __init__(self, player1, player2, result_player1=0, result_player2=0):
        self.player1 = player1
        self.player2 = player2
        self.result_player1 = result_player1
        self.result_player2 = result_player2

    def set_the_winner(self, player):
        pass

    def indicate_equality(self):
        pass

    def get_tuples(self):
        return [(self.player1, self.result_player1), (self.player2, self.result_player2)]
