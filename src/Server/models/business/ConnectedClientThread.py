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
            print(self.__clientConnection.recv(120).decode('utf-8'))
        self.__clientConnection.close()
