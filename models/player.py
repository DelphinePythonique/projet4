class Player:
    players = []
    players_counter_for_identifier = 0

    @classmethod
    def find_player_by_identifier(cls, identifier):
        player_found = None
        for player in cls.players:
            if player.identifier == identifier:
                player_found = player
        return player_found

    @classmethod
    def get_key(cls):
        return cls.ranking

    @classmethod
    def list_of_players_by_alphabetic_sort(cls):
        sorted_by_ranking = sorted(cls.players, key=lambda x: x.surname)
        return sorted_by_ranking

    @classmethod
    def list_of_players_by_ranking_sort(cls):
        sorted_by_ranking = sorted(cls.players, key=lambda x: (x.ranking, x.surname), reverse=True)
        return sorted_by_ranking
        # return sorted(sorted_by_ranking, key=attrgetter('surname'))

    def __init__(self, surname, first_name, date_of_birth, gender, ranking=None):
        Player.players_counter_for_identifier += 1
        self.identifier = Player.players_counter_for_identifier
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        Player.players.append(self)

    def set_ranking(self, value):
        self.ranking = value

    def __repr__(self):
        lines = [
            "Player:",
            f"Identifier:{self.identifier}",
            f"surname:{self.surname}",
            f"first_name:{self.first_name}",
            f"date_of_birth:{self.date_of_birth}",
            f"gender:{self.gender}",
            f"ranking:{self.ranking}",
        ]
        return "\n".join(lines)


