import workflow.tournament.draft_state as draft_state
import workflow.tournament.ready_state as ready_state
import workflow.tournament.populated_state as populated_state
import workflow.tournament.state as state


class ReadyState(state.State):
    def transition_to_draft(self) -> None:
        self.tournament.set_state(draft_state.DraftState())

    def transition_to_ready(self) -> None:
        self.tournament.set_state(ready_state.ReadyState())

    def transition_to_populated(self) -> None:
        if len(self.tournament.players) == self.tournament.get_goal_number_of_player():
            self.tournament.set_state(populated_state.PopulatedState())

    def transition_to_in_progress(self) -> None:
        pass

    def transition_to_closed(self) -> None:
        pass

    def transition_to_archived(self) -> None:
        pass

    def __str__(self):
        return f'{__name__}'
