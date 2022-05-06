def _display_players( players):
    lines = []
    ids_list = []
    for player in players:
        lines.append(f"#{player.identifier}:{player.first_name} {player.surname}({player.ranking})")
        ids_list.append(str(player.identifier))
    return lines, ids_list
