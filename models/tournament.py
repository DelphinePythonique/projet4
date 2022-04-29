from collections import Counter
from operator import itemgetter, attrgetter

from models.player import Player
from models.round import Round


class Tournament:
    DEFAULT_NUMBER_OF_ROUND = 4
    TYPE_OF_TIME_CONTROL = ("bullet", "blitz", "quick_it")
    DEFAULT_TIME_CONTROL = "blitz"
    GOAL_NUMBER_OF_PLAYERS = 8
    STATE_DRAFT = "draft"
    STATE_READY = "ready"
    STATE_IN_PROGRESS = "in_progress"
    STATE_CLOSED = "closed"
    STATE_ROUND_NO = "state_round_no"
    STATE_ROUND_STARTED = "state_round_started"
    STATE_ROUND_TO_START = "state_round_to_start"
    tournaments = []
    tournaments_counter_for_identifier = 0

    @classmethod
    def dict_to_object(cls, dict_tournament):
        if "name" in dict_tournament:
            name = dict_tournament["name"]
        if "place" in dict_tournament:
            place = dict_tournament["place"]
        if "begin_date" in dict_tournament:
            begin_date = dict_tournament["begin_date"]
        if "end_date" in dict_tournament:
            end_date = dict_tournament["end_date"]
        if "time_control" in dict_tournament:
            time_control = dict_tournament["time_control"]
        if "description" in dict_tournament:
            description = dict_tournament["description"]

        return Tournament(name, place, begin_date, end_date, time_control, description)

    @classmethod
    def find_tournament_by_identifier(cls, identifier):
        tournament_found = None
        for tournament in cls.tournaments:
            if tournament.identifier == identifier:
                tournament_found = tournament
        return tournament_found

    def __init__(
        self,
        name,
        place,
        begin_date,
        end_date,
        time_control=DEFAULT_TIME_CONTROL,
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
        self._state = self.state

        Tournament.tournaments.append(self)

    @property
    def state(self):
        if len(self.players) < Tournament.GOAL_NUMBER_OF_PLAYERS:
            self._state = Tournament.STATE_DRAFT
        elif len(self.players) == Tournament.GOAL_NUMBER_OF_PLAYERS and len(self.rounds) == 0:
            self._state = Tournament.STATE_READY

        elif len(self.rounds) > 0:
            in_progress_round, next_round = self.which_in_progress_round_and_next_round()
            if in_progress_round or next_round:
                self._state = Tournament.STATE_IN_PROGRESS
            else:
                self._state = Tournament.STATE_CLOSED
        return self._state

    @property
    def state_round(self):
        if self.state == Tournament.STATE_IN_PROGRESS:
            in_progress_round, next_round = self.which_in_progress_round_and_next_round()
            if in_progress_round:
                self._state_round = Tournament.STATE_ROUND_STARTED
            elif next_round:
                self._state_round = Tournament.STATE_ROUND_TO_START
            else:
                self._state_round = Tournament.STATE_ROUND_NO

        else:
            self._state_round = Tournament.STATE_ROUND_NO

        return self._state_round
    @property
    def active_round(self):
        in_progress_round, next_round = self.which_in_progress_round_and_next_round()
        return in_progress_round

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
            f"number_of_round:{self.number_of_round}",
        ]
        return "\n".join(lines)

    def set_time_control(self, value):
        if value in Tournament.TYPE_OF_TIME_CONTROL:
            self._time_control = value
        else:
            self._time_control = Tournament.DEFAULT_TIME_CONTROL

    def add_player(self, player):
        if self.state == Tournament.STATE_DRAFT:
            if isinstance(player, Player):
                self.players.append(player.identifier)
            elif isinstance(player, int):
                if Player.find_player_by_identifier(player):
                    self.players.append(player)

    def which_in_progress_round_and_next_round(self):
        start_rounds = [round for round in self.rounds if round.state == Round.STATE_START]
        if len(start_rounds) > 0:
            start_round = start_rounds[0]
        else:
            start_round = None
        draft_rounds = [round for round in self.rounds if round.state == Round.STATE_DRAFT]
        if len(draft_rounds) > 0:
            draft_round = draft_rounds[0]
        else:
            draft_round = None
        return start_round, draft_round

    def start_round(self):
        if self.state == Tournament.STATE_READY:
            self.generate_round()
            self.rounds[0].start(Round.RANKING_PARING_METHOD)
        elif self.state == Tournament.STATE_IN_PROGRESS:
            in_progress_round, next_round = self.which_in_progress_round_and_next_round()
            if not in_progress_round and next_round:
                next_round.start(Round.RESULT_PARING_METHOD)

    def generate_round(self):
        for i in range(1, self.number_of_round + 1):
            self.rounds.append(Round(f"Round {i}", self, i))

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
