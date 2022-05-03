from models.tournament import Tournament


class View:
    def __init__(self):
        pass

    def _display_players(self, players):
        lines = []
        for player in players:
            lines.append(f"#{player.identifier}:{player.first_name} {player.surname}({player.ranking})")
        return lines

    def index(self):
        lines = [
            "Chess tournaments managment",
            "1 - Manage players",
            "2 - Manage tournaments",
            "Enter the number of the action to be perform and press enter",
        ]
        print("\n".join(lines))
        choice = int(input())
        context = {}
        if choice == 1:
            context["route"] = "index_players"
        else:
            context["route"] = "index_tournaments"
        return context

    def index_player(self, players):
        # Display players and return choice menu between new player , update ranking player, menu index
        lines = ["Chess tournaments managment - Players", "1 - Add player"]
        if len(players) > 0:
            lines.append("2 - Update Ranking")
            lines.append("3 - Homepage")
            lines.append("========================================")
            lines.append("PLAYERS")
            lines.append("========================================")
            lines.extend(self._display_players(players))
        lines.append("Enter the number of the action to be perform and press enter")
        print("\n".join(lines))

        choice = int(input())
        context = {}
        if choice == 1:
            context["route"] = "add_player"
        elif choice == 2:
            context["route"] = "update_ranking_player"
            print("Enter player identifier")
            context["player_id"] = input()
        else:
            context["route"] = "homepage"
        return context

    def add_player(self, context):
        # with view asks for the entry of the information of the new player and return save message with index_player
        context = {"player": {}}
        print("Enter player informations")
        print("Enter surname")
        context["player"]["surname"] = input()
        print("Enter first_name")
        context["player"]["first_name"] = input()
        print("Enter date_of_birth as DD/MM/YYYY")
        context["player"]["date_of_birth"] = input()
        print("Enter gender as f:feminine, m:masculine, o:other")
        context["player"]["gender"] = input()
        print("Enter player's ranking")
        context["player"]["ranking"] = input()
        context["route"] = "index_players"
        return context

    def update_ranking_player(self, context):
        # with view asks for the new ranking of the player and return save message with index_player
        if "player" in context:
            print(context["player"])
        print("Enter new_ranking")
        context["player"].ranking = int(input())
        context["route"] = "index_players"
        return context

    def index_tournament(self, tournaments):
        # Display tournaments and return choice menu between new tournament, display tournament, menu index
        # Display players and return choice menu between new player , update ranking player, menu index
        lines = ["Chess tournaments managment - Tournament", "1 - Add tournament"]
        if len(tournaments) > 0:
            lines.append("2 - Display tournament")
            lines.append("3 - Homepage")
            lines.append("========================================")
            lines.append("TOURNAMENTS")
            lines.append("========================================")
        for tournament in tournaments:
            lines.append(f"{tournament.identifier}:{tournament.name} ({tournament.state})")
        lines.append("Enter the number of the action to be perform and press enter")
        print("\n".join(lines))

        choice = int(input())
        context = {}
        if choice == 1:
            context["route"] = "add_tournament"
        elif choice == 2:
            context["route"] = "display_tournament"
            print("Enter tournament identifier")
            context["tournament_id"] = input()
        else:
            context["route"] = "homepage"
        return context

    def add_tournament(self, context):
        # with view asks for the entry of the information of the new tournament and return save message with index tournament

        context = {"tournament": {}}
        print("Enter tournament informations")
        print("Enter name")
        context["tournament"]["name"] = input()
        print("Enter description")
        context["tournament"]["description"] = input()
        print("Enter place")
        context["tournament"]["place"] = input()
        print("Enter begin date as DD/MM/YYYY")
        context["tournament"]["begin_date"] = input()
        print("Enter end date as DD/MM/YYYY")
        context["tournament"]["end_date"] = input()
        print(f"Enter time control among {Tournament.TYPE_OF_TIME_CONTROL} ")
        context["tournament"]["time_control"] = input()
        context["route"] = "index_tournaments"
        return context

    def display_tournament(self, context):
        # display tournament, return menu choice between start_round, add player, save result match
        if "tournament" in context:
            tournament = context["tournament"]

        lines = [f"Chess tournaments managment - Tournament{tournament.name}"]
        if tournament.state == Tournament.STATE_DRAFT:
            lines.append("1 - add Player")
        if tournament.state == Tournament.STATE_READY:
            lines.append("2 - start round")
        if tournament.state == Tournament.STATE_IN_PROGRESS:
            if tournament.state_round == Tournament.STATE_ROUND_STARTED:
                lines.append("3 - save result")
            elif tournament.state_round == Tournament.STATE_ROUND_TO_START:
                lines.append("2 - start round")
        lines.append("4 - Homepage")
        lines.append("======================================================================================")
        lines.append(
            f"Tournament {tournament.name} from {tournament.begin_date} to {tournament.end_date} at {tournament.place}"
        )
        lines.append("--------------------------------------------------------------------------------------")
        players_str = " ".join(str(tournament.players))
        lines.append(players_str)
        for round in tournament.rounds:
            status = ""
            if round == tournament.active_round:
                status = "open"
            lines.append(f"Round {round.name} {status}")
            lines.append("---------------------")
            for match in round.matchs:
                lines.append(
                    f"match #{round.matchs.index(match)+1}:Player #1:{match[0][0].surname} ({match[0][0].ranking}) - Result:{match[0][1]} /"
                    f"Player #2 {match[1][0].surname} ({match[1][0].ranking}) - Result:{match[1][1]}"
                )
        lines.append("Enter the number of the action to be perform and and press enter")
        print("\n".join(lines))

        choice = int(input())
        context = {}
        if choice == 1:
            context["route"] = "add_player_into_tournament"
            context["tournament"] = tournament
        elif choice == 2:
            context["route"] = "start_round"
            context["tournament"] = tournament
        elif choice == 3:
            context["route"] = "save_round"
            context["tournament"] = tournament
            print("For which match do you want save result?")
            match_number = int(input())
            context['match'] = tournament.active_round.matchs[match_number - 1]
            print("Enter the result 0: equality, 1: winner is player one, 2: winner is player 2")
            match_result = int(input())
            context['match_result'] = match_result
        else:
            context["route"] = "homepage"
        return context

    def add_player_into_tournament(self, context):
        if "tournament" in context:
            tournament = context["tournament"]
            if "players" in context:
                players = context["players"]
                lines = ["Select players identifiers separated by ,"]
                lines.extend(self._display_players(players))
                print("\n".join(lines))
                context["tournament"] = tournament
                context["tournament_id"] = tournament.identifier
                context["player_ids"] = input()
                context["route"] = "display_tournament"
            else:
                context["route"] = "display_tournament"
        else:
            context["route"] = "index_tournaments"
        return context
