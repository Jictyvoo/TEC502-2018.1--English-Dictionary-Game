import threading


class ConnectedClientThread(threading.Thread):
    def __init__(self, client_connection, client_address, room_controller_thread):
        threading.Thread.__init__(self)
        self.__clientConnection = client_connection
        self.__clientAddress = client_address
        self.__room_controller_thread = room_controller_thread

    def run(self):
        message = self.__clientConnection.recv(13).decode('utf-8')
        if message == "request_rooms":
            rooms = self.__room_controller_thread.get_rooms()
            for room in rooms:
                self.__clientConnection.send(bytes(room, 'utf-8'))
        elif message == "creating_room":
            room_status = self.__clientConnection.recv(150).decode('utf-8').split("|_-_|")
            client_address = "%s:%d" % self.__clientAddress
            command = "new_room|_-_|" + client_address + "|_-_|" + room_status[0] + "|_-_|" + room_status[1] + "|_-_|" + \
                      room_status[2] + "|_-_|" + room_status[3]
            self.__room_controller_thread.execute_command(command)
        elif message == "players_names":
            room_name = self.__clientConnection.recv(65).decode('utf-8')
            players_names = self.__room_controller_thread.get_players_names(room_name)
            print("Sending Players Names %s" % "|_|".join(players_names))
            self.__clientConnection.send(bytes(str("|_|".join(players_names)), 'utf-8'))
        elif message == "joining__room":
            information = self.__clientConnection.recv(65).decode('utf-8').split("|_-_|")
            room_name = information[0]
            password = information[1]
            player_name = information[2]
            added = self.__room_controller_thread.add_player_in_room(room_name, password, self.__clientAddress,
                                                                     player_name)
            self.__clientConnection.send(bytes(added and "Successful" or "Error", 'utf-8'))
        elif message == "start__gaming":
            from Client.util.DiceManipulator import DiceManipulator
            dices = DiceManipulator()
            send_string = "|_|".join(dices.randomize())
            self.__clientConnection.send(bytes(send_string, 'utf-8'))
        self.__clientConnection.close()
