import router
from utils.input_utils import inputs_request


class ReportTournamentRoundsView:
    def display(self, context):
        tournament = context["tournament"]
        lines = [
            f"Chess tournaments managment - Rounds of tournament {context['tournament']}",
        ]

        lines.extend([
            f"{router.Router.REPORT_INDEX_ID} - Menu Report",
            f"{router.Router.REPORT_TOURNAMENT_ID} - Report Tournament",
            "Enter the number of the action to be perform and press enter",
        ])
        for round_ in tournament.rounds:
            # if round_ == tournament.active_round:

            lines.append(f"Round {round_.name} {round_.state}")
        inputs_required = {
            "menu": {
                "question": lines,
                "type": str,
                "not_null": True,
                "constraints": {"choice_ids": [router.Router.REPORT_INDEX_ID, router.Router.REPORT_TOURNAMENT_ID]},
            },
        }

        context = inputs_request(inputs_required, context_key="choice", context=context)
        context["route_id"] = context["choice"]["menu"]
        return context
