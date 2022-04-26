from abc import ABC, abstractmethod


class State(ABC):
    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, round) -> None:
        self._round = round

    @abstractmethod
    def transition_to_draft(self) -> None:
        pass

    @abstractmethod
    def transition_to_start(self) -> None:
        pass

    @abstractmethod
    def transition_to_stop(self) -> None:
        pass

    def __str__(self):
        return f'{__name__}'



