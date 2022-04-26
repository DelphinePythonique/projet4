import workflow.round.state as state
import workflow.tournament.populated_state as populated_state
import workflow.tournament.in_progress_state as in_progress_state
import workflow.round.start_state as start_state


class DraftState(state.State):
    def transition_to_draft(self) -> None:
        pass

    def transition_to_start(self) -> None:
        if isinstance(self.round.tournament.present_state(), populated_state.PopulatedState):
            self.round.set_state(start_state.StartState)
            self.round.do_the_paring()
            self.round.tournament.set_state(in_progress_state.InProgressState)

    def transition_to_stop(self) -> None:
        pass
