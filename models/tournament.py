from models.player import Player
from models.round import Round
from workflow.Tournament.draft_state import DraftState
from workflow.Tournament.ready_state import ReadyState

DEFAULT_NUMBER_OF_ROUND = 4
TYPE_OF_TIME_CONTROL = ("bullet", "blitz", "quick_it")
DEFAULT_STATE = DraftState()
READY_STATE = ReadyState()


class Tournament:

    tournaments = []
    tournaments_counter_for_identifiant = 0

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
            state=DEFAULT_STATE,
            description=None,
            number_of_round=DEFAULT_NUMBER_OF_ROUND,
    ):
        """

        :type time_control: str
        """

        Tournament.tournaments_counter_for_identifiant += 1
        self.identifiant = Tournament.tournaments_counter_for_identifiant
        self.name = name
        self.set_tournament(state)
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
        return (
            "Tournament:\n"
            f"Identifiant:{self.identifiant}\n"
            f"name:{self.name}\n"
            f"state:{self._state}\n"
            f"place:{self.place}\n"
            f"begin_date:{self.begin_date}\n"
            f"end_date:{self.end_date}\n"
            f"time_control:{self._time_control}\n"
            f"description:{self.description}\n"
            f"number_of_round:{self.number_of_round}\n"
        )

    def set_tournament(self, state):
        self._state = state
        self._state.tournament = self

    def present_state(self):
        return self._state

    def set_time_control(self, value):
        if value in TYPE_OF_TIME_CONTROL:
            self._time_control = value
        else:
            raise ValueError(f'Time_control must be in {TYPE_OF_TIME_CONTROL}')

    def get_state(self):
        return self._state

    def set_state(self, value):
        self._state = value

    def transition_to_draft(self):
        self._state.transition_to_draft()

    def transition_to_ready(self):
        self._state.transition_to_ready()

    def transition_to_populated(self):
        self._state.transition_to_populated()

    def transition_to_in_progress(self):
        self._state.transition_to_in_progress()

    def transition_to_in_closed(self):
        self._state.transition_to_closed()

    def transition_to_in_archived(self):
        self._state.transition_to_closed()

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player.identifiant)
        elif isinstance(player, int):
            if Player.find_player_by_identifiant(player):
                self.players.append(player)
            else:
                raise ValueError("no player under this identifiant")
        else:
            raise ValueError("is not a player")

    def generate_round(self):
        for i in range(1, self.number_of_round + 1):
            self.rounds.append(Round(f"Round {i}"))
            print(self.rounds[i - 1])
