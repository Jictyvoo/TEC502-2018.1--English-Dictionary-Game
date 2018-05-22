from Server.models.value.Room import Room


class RoomsController:
    def __init__(self):
        from Server.util.MulticastAddressGenerator import MulticastAddressGenerator
        self.__multicast_generator_address = MulticastAddressGenerator()
        self.__existent_rooms = {}

    def new_room(self, room_name, coordinator_ip):
        if room_name + coordinator_ip in self.__existent_rooms.keys():
            if not self.__existent_rooms[room_name + coordinator_ip]:
                temp_room = Room(self.__multicast_generator_address.get_next_group(), room_name, coordinator_ip)
                self.__existent_rooms[room_name + coordinator_ip] = temp_room
                return temp_room
            return None
        return None

    def change_coordinator(self, room_name, previous_coordinator, new_coordinator):
        if room_name + previous_coordinator in self.__existent_rooms.keys():
            self.__existent_rooms[room_name + previous_coordinator].set_coordinator_player_address(new_coordinator)

    def remove_room(self):
        for key, value in self.__existent_rooms:
            if value.get_amount_players() == 0:
                self.__existent_rooms[key] = None
