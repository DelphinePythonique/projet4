import views.view as view
import router
from utils.input_utils import inputs_request
from views.tournament._utils import _format_display_tournaments


class TournamentIndexView:
    def display(self, context):
        tournaments = []
        ids_tournaments = []
        menu_items = [router.Router.ADD_TOURNAMENT_ID]
        if "tournaments" in context:
            tournaments = context["tournaments"]
        # Display tournaments and return choice menu between new tournament, display tournament, menu index
        # Display players and return choice menu between new player , update ranking player, menu index

        lines = ["Chess tournaments managment - Tournament", view.View.SEPARATOR, "Tournaments"]
        tournament_lines, ids_tournaments = _format_display_tournaments(tournaments)
        lines.extend(tournament_lines)
        lines.extend([view.View.SEPARATOR, f"{router.Router.ADD_TOURNAMENT_ID} - Add Tournament"])
        if len(tournaments) > 0:
            lines.extend(
                [
                    f"{router.Router.DISPLAY_TOURNAMENT_ID} - Display tournament",
                    f"{router.Router.HOMEPAGE_ID} - Homepage",
                    view.View.SEPARATOR,

                ]
            )
            menu_items.extend([router.Router.DISPLAY_TOURNAMENT_ID, router.Router.HOMEPAGE_ID])

        lines.append("Enter the number of the action to be perform and press enter")

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
        if context["route_id"] == router.Router.DISPLAY_TOURNAMENT_ID:
            inputs_required = {
                "tournament_identifier": {
                    "question": ["Enter tournament identifier"],
                    "type": str,
                    "not_null": True,
                    "constraints": {"choice_ids": ids_tournaments},
                },
            }

            context = inputs_request(inputs_required, context_key="choice", context=context)
            context["tournament_id"] = context["choice"]["tournament_identifier"]

        return context
