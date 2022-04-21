from workflow.Tournament.ready_state import ReadyState
from workflow.Tournament.state import State


class DraftState(State):
    def transition_to_draft(self) -> None:
        pass

    def transition_to_ready(self) -> None:
        self.tournament.set_state(ReadyState)

    def transition_to_populated(self) -> None:
        pass

    def transition_to_in_progress(self) -> None:
        pass

    def transition_to_closed(self) -> None:
        pass

    def transition_to_archived(self) -> None:
        pass

    def __str__(self):
        return f'{__name__}'
