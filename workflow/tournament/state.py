from abc import ABC, abstractmethod


class State(ABC):
    @property
    def tournament(self):
        return self._tournament

    @tournament.setter
    def tournament(self, tournament) -> None:
        self._tournament = tournament

    @abstractmethod
    def transition_to_draft(self) -> None:
        pass

    @abstractmethod
    def transition_to_ready(self) -> None:
        pass

    @abstractmethod
    def transition_to_populated(self) -> None:
        pass

    @abstractmethod
    def transition_to_in_progress(self) -> None:
        pass

    @abstractmethod
    def transition_to_closed(self) -> None:
        pass

    @abstractmethod
    def transition_to_archived(self) -> None:
        pass

    def __str__(self):
        return f'{__name__}'



