import workflow.tournament.ready_state as ready_state
import workflow.tournament.state as state


class DraftState(state.State):
    def transition_to_draft(self) -> None:
        pass

    def transition_to_ready(self) -> None:
        self.tournament.set_state(ready_state.ReadyState())
        if len(self.tournament.players) == self.tournament.get_goal_number_of_player():
            self.tournament.transition_to_populated()

    def transition_to_populated(self) -> None:
        raise ValueError('is not possible to pass directly draft to populated, it must be notified as ready')

    def transition_to_in_progress(self) -> None:
        raise ValueError('is not possible to pass directly draft to in_progress, it must be notified as ready')

    def transition_to_closed(self) -> None:
        raise ValueError('is not possible to pass directly draft to closed')

    def transition_to_archived(self) -> None:
        raise ValueError('is not possible to pass directly draft to archived')

    def __str__(self):
        return f'{__name__}'
