from views import view


def _format_display_players(players):
    lines = []
    ids_list = []
    lines.append(f"{'id#'.ljust(5)}|{'first name'.ljust(50)}|{'surname'.ljust(50)}|{'ranking'.ljust(7)}|")
    lines.append(view.View.SEPARATOR)
    for player in players:
        lines.append(f"{str(player.identifier).ljust(5)}|{player.first_name.ljust(50)}|{player.surname.ljust(50)}|{str(player.ranking).ljust(7)}")
        ids_list.append(str(player.identifier))
    return lines, ids_list
