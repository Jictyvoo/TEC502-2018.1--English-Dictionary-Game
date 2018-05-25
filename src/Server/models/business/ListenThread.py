import json.decoder as decoder_json
import socket

from Server.models.business.ConnectedClientThread import ConnectedClientThread


class ListenThread:
    def __init__(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with open("config.conf", 'r') as content_file:
            decoder = decoder_json.JSONDecoder()
            decoded = decoder.decode(content_file.read())
            host = decoded['host']
            port = int(decoded['port'])
        server_address = (host, port)
        self.__socket.bind(server_address)
        # listen() puts the socket into server mode
        self.__socket.listen(1000)
        from Server.controllers.RoomsController import RoomsController
        self.__room_controller_thread = RoomsController()
        # self.__remove_room_thread = threading.Thread(target=self.__room_controller.remove_room)

    def main_execution(self):
        self.__room_controller_thread.start()
        while True:
            # Wait for a connection
            print("Listening Clients")
            connection, client_address = self.__socket.accept()
            print("Connection Address", client_address)
            connected_client = ConnectedClientThread(connection, client_address, self.__room_controller_thread)
            connected_client.start()
