import views.view as view
import router
from utils.input_utils import inputs_request


class TournamentIndexView:
    def index(self, context):
        tournaments = []
        ids_tournaments = []
        menu_items = [router.Router.ADD_TOURNAMENT_ID]
        if "tournaments" in context:
            tournaments = context["tournaments"]
        # Display tournaments and return choice menu between new tournament, display tournament, menu index
        # Display players and return choice menu between new player , update ranking player, menu index

        lines = ["Chess tournaments managment - Tournament", view.View.SEPARATOR, "Tournaments"]
        for tournament in tournaments:
            lines.append(f"{tournament.identifier}:{tournament.name} ({tournament.state})")
            ids_tournaments.append(str(tournament.identifier))
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

        if context["choice"]["menu"] == router.Router.ADD_TOURNAMENT_ID:
            context = {"route": router.Router.ADD_TOURNAMENT}
        elif context["choice"]["menu"] == router.Router.DISPLAY_TOURNAMENT_ID:
            context["route"] = router.Router.DISPLAY_TOURNAMENT
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

        else:
            context["route"] = router.Router.HOMEPAGE_ID
        return context
