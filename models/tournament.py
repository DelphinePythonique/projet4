from collections import Counter
from operator import itemgetter

from models.player import Player
from models.round import Round


class Tournament:
    DEFAULT_NUMBER_OF_ROUND = 4
    TYPE_OF_TIME_CONTROL = ("bullet", "blitz", "quick_it")
    GOAL_NUMBER_OF_PLAYERS = 8

    tournaments = []
    tournaments_counter_for_identifier = 0

    @classmethod
    def list_of_tournament(cls):
        pass

    def __init__(
            self,
            name,
            place,
            begin_date,
            end_date,
            time_control,
            description=None,
            number_of_round=DEFAULT_NUMBER_OF_ROUND,
    ):
        """

        :type time_control: str
        """

        Tournament.tournaments_counter_for_identifier += 1
        self.identifier = Tournament.tournaments_counter_for_identifier
        self.name = name
        self.place = place
        self.begin_date = begin_date
        self.end_date = end_date
        self.number_of_round = number_of_round
        self.rounds = []
        self.players = []
        self.set_time_control(time_control)
        self.description = description
        Tournament.tournaments.append(self)

    def __str__(self):
        lines = [
            "tournament:",
            f"Identifier:{self.identifier}",
            f"name:{self.name}",
            f"place:{self.place}",
            f"begin_date:{self.begin_date}",
            f"end_date:{self.end_date}",
            f"time_control:{self._time_control}",
            f"description:{self.description}",
            f"number_of_round:{self.number_of_round}"
        ]
        return "\n".join(lines)

    def set_time_control(self, value):
        if value in Tournament.TYPE_OF_TIME_CONTROL:
            self._time_control = value
        else:
            raise ValueError(f"Time_control must be in {Tournament.TYPE_OF_TIME_CONTROL}")

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player.identifier)
        elif isinstance(player, int):
            if Player.find_player_by_identifier(player):
                self.players.append(player)
            else:
                raise ValueError("no player under this identifier")
        else:
            raise ValueError("is not a player")

    def generate_round(self):
        for i in range(1, self.number_of_round + 1):
            self.rounds.append(Round(f"Round {i}", self))

    def get_goal_number_of_player(self):
        return Tournament.GOAL_NUMBER_OF_PLAYERS

    def extract_tournament_player_sort_by_ranking(self):
        tournament_players_order_by_ranking = [
            player for player in Player.list_of_players_by_ranking_sort() if player.identifier in self.players
        ]
        return tournament_players_order_by_ranking

    def extract_tournament_player_sort_by_alphabetic(self):
        tournament_players_order_by_alphabetic = [
            player for player in Player.list_of_players_by_alphabetic_sort() if player.identifier in self.players
        ]
        return tournament_players_order_by_alphabetic

    def get_total_result_of_players(self):
        result = Counter()
        for round in self.rounds:
            result.update(dict(round.get_result_of_players()))

        tuple_result = [(k, v) for k, v in result.items()]

        return tuple_result

    def extract_tournament_player_sort_by_result(self):
        total_result_of_players_tuple = self.get_total_result_of_players()
        total_result_of_players_tuple_order_by_alpha = sorted(
            total_result_of_players_tuple, key=lambda player: player[0].surname
        )
        total_result_of_players_tuple_order_by_result = sorted(
            total_result_of_players_tuple_order_by_alpha, key=itemgetter(1), reverse=True
        )

        return total_result_of_players_tuple_order_by_result
