def _format_display_tournaments(tournaments):
    lines = []
    ids_tournaments = []
    for tournament in tournaments:
        lines.append(f"{tournament.identifier}:{tournament.name} ({tournament.state})")
        ids_tournaments.append(str(tournament.identifier))
    return lines, ids_tournaments


def _format_matchs(round_):
    match_ids = []
    lines = []
    num_match = 1
    if len(round_.matchs) > 0:
        lines.append(f"{'#'.ljust(5)}|{'Player1'.ljust(72)}|{'Player2'.ljust(70)}")
        lines.append(
            f"{''.ljust(5)}|{'surname'.ljust(50)}|{'ranking'.ljust(10)}|{'result'.ljust(10)}|{'surname'.ljust(50)}|{'ranking'.ljust(10)}|{'result'.ljust(10)}"
        )

    for match in round_.matchs:
        match_ids.append(str(num_match))
        lines.append(
            f"{str(num_match).ljust(5)}|{match[0][0].surname.ljust(50)}|{str(match[0][0].ranking).ljust(10)}|"
            f"{str(match[0][1]).ljust(10)}|"
            f"{match[1][0].surname.ljust(50)}|{str(match[1][0].ranking).ljust(10)}|{str(match[1][1]).ljust(10)}"
        )
        num_match += 1
    return lines, match_ids
