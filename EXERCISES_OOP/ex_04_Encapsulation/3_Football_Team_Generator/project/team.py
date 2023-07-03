from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player_name == player.name:
            # if player_name not in self.__players: why not this code
                self.__players.remove(player)
                return player
        return f"Player {player_name} not found"





