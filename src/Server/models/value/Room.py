class Room:
    def __init__(self, multicast_ip=None, name="Pseudo-Room", coordinator_player_address=None, limit_players=2,
                 password=""):
        self.__room_ip = multicast_ip
        self.__name = name
        self.__coordinator_player_address = coordinator_player_address
        self.__limit_players = limit_players
        self.__current_players = {coordinator_player_address: True}
        self.__password = password

    def get_room_ip(self):
        return self.__room_ip

    def set_room_ip(self, room_ip):
        self.__room_ip = room_ip

    def get_name(self):
        return self.__name

    def get_coordinator_player_address(self):
        return self.__coordinator_player_address

    def set_coordinator_player_address(self, coordinator_player):
        self.__coordinator_player_address = coordinator_player

    def get_limit_players(self):
        return self.__limit_players

    def remove_player(self, player_address):
        if player_address in self.__current_players.keys():
            self.__current_players[player_address] = False

    def add_player(self, player_address):
        self.__current_players[player_address] = True

    def get_amount_players(self):
        count = 0
        for key in self.__current_players.keys():
            if self.__current_players[key]:
                count += 1
        return count
