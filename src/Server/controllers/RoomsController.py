import threading

from Server.models.value.Room import Room


class RoomsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        from Server.util.MulticastAddressGenerator import MulticastAddressGenerator
        self.__multicast_generator_address = MulticastAddressGenerator()
        self.__existent_rooms = {}
        self.__stackCommands = []

    def __lambda_creation_room(self, coordinator_ip, room_name, amount_of_players, password):
        temp_room = Room(self.__multicast_generator_address.get_next_group(), room_name, coordinator_ip,
                         amount_of_players, password)
        self.__existent_rooms[room_name + coordinator_ip] = temp_room
        return temp_room

    def __new_room(self, coordinator_ip, room_name, amount_of_players, password):
        if room_name + coordinator_ip in self.__existent_rooms.keys():
            if not self.__existent_rooms[room_name + coordinator_ip]:
                return self.__lambda_creation_room(coordinator_ip, room_name, amount_of_players, password)
            return None
        else:
            return self.__lambda_creation_room(coordinator_ip, room_name, amount_of_players, password)

    def __change_coordinator(self, room_name, previous_coordinator, new_coordinator):
        if room_name + previous_coordinator in self.__existent_rooms.keys():
            self.__existent_rooms[room_name + previous_coordinator].set_coordinator_player_address(new_coordinator)

    def __remove_room(self):
        for key in self.__existent_rooms.keys():
            value = self.__existent_rooms[key]
            if value:
                if value.get_amount_players() == 0:
                    self.__existent_rooms[key] = None

    def get_rooms(self):
        return_list = []
        for key in self.__existent_rooms:
            room = self.__existent_rooms[key]
            if room:
                string_room = room.get_name() + ": " + str(room.get_amount_players()) + "/" + str(
                    room.get_limit_players()) + "|_|" + room.get_coordinator_player_address()
                return_list.append(string_room)
        return tuple(return_list)

    def execute_command(self, command):
        self.__stackCommands.append(command)

    def run(self):
        while True:
            self.__remove_room()
            if self.__stackCommands:
                command = self.__stackCommands.pop().split("|_-_|")
                if command[0] == "new_room":
                    self.__new_room(command[1], command[2], command[3], command[4])
                elif command[0] == "change_coordinator":
                    self.__change_coordinator(command[1], command[2], command[3])
