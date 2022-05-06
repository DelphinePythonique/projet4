from models.player import Player
from models.tournament import Tournament
from utils.input_utils import inputs_request
import views.view as view


class TournamentDisplayView():
    def display(self, context):
        # display tournament, return menu choice between start_round, add player, save result match
        if "tournament" in context:
            tournament = context["tournament"]
        menu_items = ["4"]
        lines = [f"Chess tournaments managment - Tournament{tournament.name}"]
        if tournament.state == Tournament.STATE_DRAFT:
            lines.append("1 - add Player")
            menu_items.append("1")

        if tournament.state == Tournament.STATE_READY:
            lines.append("2 - start round_")
            menu_items.append("2")

        if tournament.state == Tournament.STATE_IN_PROGRESS:
            if tournament.state_round == Tournament.STATE_ROUND_STARTED:
                lines.append("3 - save result")
                menu_items.append("3")

            elif tournament.state_round == Tournament.STATE_ROUND_TO_START:
                lines.append("2 - start round_")
                menu_items.append("2")
        lines.extend(
            [
                "4 - Homepage",
                view.View.SEPARATOR,
                f"Tournament {tournament.name} " f"from {tournament.begin_date} ",
                f"to {tournament.end_date} at {tournament.place}",
                view.View.SEPARATOR,
                "Players ",
            ]
        )

        for player_id in tournament.players:
            player = Player.find_player_by_identifier(player_id)
            lines.append(f"{player.first_name} {player.surname}(r:{player.ranking})")

        for round_ in tournament.rounds:
            status = ""
            if round_ == tournament.active_round:
                status = "open"
            lines.append(f"Round {round_.name} {status}")
            lines.append("---------------------")
            for match in round_.matchs:
                lines.append(
                    f"match #{round_.matchs.index(match) + 1}:Player #1:{match[0][0].surname} ({match[0][0].ranking}) - Result:{match[0][1]} /"
                    f"Player #2 {match[1][0].surname} ({match[1][0].ranking}) - Result:{match[1][1]}"
                )
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

        choice = context["choice"]["menu"]
        context = {}
        if choice == "1":
            context.update({"route": "add_player_into_tournament", "tournament": tournament})
        elif choice == "2":
            context.update({"route": "start_round", "tournament": tournament})

        elif choice == "3":
            context.update({"route": "save_round", "tournament": tournament})
            print("For which match do you want save result?")
            match_number = int(input())
            context["match"] = tournament.active_round.matchs[match_number - 1]
            print("Enter the result 0: equality, 1: winner is player one, 2: winner is player 2")
            match_result = int(input())
            context["match_result"] = match_result
        else:
            context["route"] = "homepage"
        return context
