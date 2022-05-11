from typing import TYPE_CHECKING

from models.tournament import Tournament
from utils.input_utils import inputs_request
from views.tournament._utils import _format_matchs

if TYPE_CHECKING:
    from views.view import View


class TournamentDisplayView:

    def __init__(self, view: "View"):
        self._view = view

    @property
    def view(self):
        return self._view

    @property
    def router(self):
        return self._view.router

    def display(self, context):
        # display tournament, return menu choice between start_round, add player, save result match
        if "tournament" in context:
            tournament = context["tournament"]
            menu_items = [self.router.HOMEPAGE_ID]
            match_ids = []
            lines = [f"Chess tournaments managment - Tournament{tournament.name}"]

            lines.extend(
                [
                    self.view.SEPARATOR,
                    f"Tournament {tournament.name} " f"from {tournament.begin_date} ",
                    f"to {tournament.end_date} at {tournament.place}",
                    self.view.SEPARATOR,
                    "Players ",
                ]
            )
            for player in context["tournament_players"]:
                lines.append(f"{player.first_name} {player.surname}(r:{player.ranking})")

            for round_ in tournament.rounds:

                lines.append(f"Round {round_.name} {round_.state}")
                lines.append("---------------------")
                matchs_lines, match_ids = _format_matchs(round_)
                lines.extend(matchs_lines)

            lines.extend([self.view.SEPARATOR, f"{self.router.HOMEPAGE_ID} - Homepage"])
            if tournament.state == Tournament.STATE_DRAFT:
                lines.append(f"{self.router.ADD_PLAYER_INTO_TOURNAMENT_ID} - add Player")
                menu_items.append(self.router.ADD_PLAYER_INTO_TOURNAMENT_ID)

            if tournament.state == Tournament.STATE_READY:
                lines.append(f"{self.router.START_ROUND_ID} - start round")
                menu_items.append(self.router.START_ROUND_ID)

            if tournament.state == Tournament.STATE_IN_PROGRESS:
                if tournament.state_round == Tournament.STATE_ROUND_STARTED:
                    lines.append(f"{self.router.SAVE_ROUND_ID} - save result")
                    menu_items.append(self.router.SAVE_ROUND_ID)

                elif tournament.state_round == Tournament.STATE_ROUND_TO_START:
                    lines.append(f"{self.router.START_ROUND_ID} - start round")
                    menu_items.append(self.router.START_ROUND_ID)

            lines.append("Enter the number of the action to be perform and and press enter")
            inputs_required = {
                "menu": {
                    "question": lines,
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": menu_items},
                },
            }

            context = inputs_request(inputs_required, context_key="choice", context=context)

            context["route_id"] = context["choice"]["menu"]

            if context["route_id"] in [self.router.ADD_PLAYER_INTO_TOURNAMENT_ID, self.router.START_ROUND_ID, self.router.SAVE_ROUND_ID]:
                context.update({"tournament": tournament})

            if context["route_id"] == self.router.SAVE_ROUND_ID:
                context.update({"tournament": tournament})
                inputs_required = {
                    "menu": {
                        "question": ["For which match do you want save result?"],
                        "type": str,
                        "not_null": True,
                        "constraints": {"choice_ids": match_ids},
                    },
                }

                context = inputs_request(inputs_required, context_key="choice", context=context)

                match_number = context['choice']['menu']
                context["match"] = tournament.active_round.matchs[int(match_number) - 1]

                inputs_required = {
                    "result": {
                        "question": ["Enter the result 0: equality, 1: winner is player one, 2: winner is player 2"],
                        "type": str,
                        "not_null": True,
                        "constraints": {"choice_ids": ["0", "1", "2"]},
                    },
                }

                context = inputs_request(inputs_required, context_key="choice", context=context)

                match_result = context["choice"]["result"]
                context["match_result"] = match_result

        return context
