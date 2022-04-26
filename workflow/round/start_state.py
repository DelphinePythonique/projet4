import workflow.round.state as state


class StartState(state.State):
    def transition_to_draft(self) -> None:
        pass

    def transition_to_start(self) -> None:
        pass

    def transition_to_stop(self) -> None:
        pass
