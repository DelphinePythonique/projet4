from tinydb import TinyDB
from tinydb.table import Document


class Player:
    players = []
    players_counter_for_identifier = 0
    db = TinyDB("db.json")
    player_table = db.table("players")

    @classmethod
    def upload_players(self):
        serialized_players = Player.player_table.all()
        for serialized_player in serialized_players:
            Player(
                surname=serialized_player["surname"],
                first_name=serialized_player["first_name"],
                date_of_birth=serialized_player["date_of_birth"],
                gender=serialized_player["gender"],
                ranking=serialized_player["ranking"],
            )

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
        sorted_by_alphabetic = sorted(cls.players, key=lambda x: x.surname)
        return sorted_by_alphabetic

    @classmethod
    def list_of_players_by_ranking_sort(cls):
        sorted_by_ranking = sorted(cls.players, key=lambda x: (x.ranking, x.surname), reverse=True)
        return sorted_by_ranking
        # return sorted(sorted_by_ranking, key=attrgetter('surname'))

    @classmethod
    def dict_to_object(cls, dict_player):

        if "surname" in dict_player:
            surname = dict_player["surname"]
        if "first_name" in dict_player:
            first_name = dict_player["first_name"]
        if "date_of_birth" in dict_player:
            date_of_birth = dict_player["date_of_birth"]
        if "gender" in dict_player:
            gender = dict_player["gender"]
        if "ranking" in dict_player:
            ranking = dict_player["ranking"]

        return Player(surname, first_name, date_of_birth, gender, ranking)

    def __init__(self, surname, first_name, date_of_birth, gender, ranking=None):
        Player.players_counter_for_identifier += 1
        self.identifier = Player.players_counter_for_identifier
        self.surname = surname
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        Player.players.append(self)

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        self._ranking = value

    def serialized_player(self):
        serialized_player = {
            "Identifier": self.identifier,
            "surname": self.surname,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
        }
        return serialized_player

    def save(self):
        Player.player_table.insert(Document(self.serialized_player(), doc_id=self.identifier))

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
