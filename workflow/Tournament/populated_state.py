from workflow.Tournament.state import State


class PopulatedState(State):
    def transition_to_draft(self) -> None:
        pass

    def transition_to_ready(self) -> None:
        pass

    def transition_to_populated(self) -> None:
        pass

    def transition_to_in_progress(self) -> None:
        pass

    def transition_to_closed(self) -> None:
        pass

    def transition_to_archived(self) -> None:
        pass
