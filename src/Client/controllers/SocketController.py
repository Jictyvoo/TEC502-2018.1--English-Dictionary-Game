# example from https://pymotw.com/3/socket/multicast.html
import socket
import struct
import json.decoder as decoder_json


class SocketController:
    def __init__(self):
        self.__multicast_group = '224.3.29.71'
        with open("../config.conf", 'r') as content_file:
            decoder = decoder_json.JSONDecoder()
            decoded = decoder.decode(content_file.read())
            self.__host = decoded['host']
            self.__port = int(decoded['port'])
        self.__server_address = (self.__host, self.__port)
        # Create the socket
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind to the server address
        # self.__socket.bind(self.__server_address)

    def add_socket_multicast(self):
        # Tell the operating system to add the socket to
        # the multicast group on all interfaces.
        group = socket.inet_aton(self.__multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.__socket.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            mreq)

    def __reset_socket(self):
        self.__socket.close()
        self.__server_address = (self.__host, self.__port)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get_rooms(self):
        self.__socket.connect(self.__server_address)
        message = bytes("request_rooms", 'utf-8')
        self.__socket.send(message)

        existent_rooms = []
        while True:
            message = self.__socket.recv(65)
            if message:
                existent_rooms.append(message.decode('utf-8').split("|_|"))
            else:
                break
        self.__reset_socket()
        return existent_rooms

    def create_room(self, room_name, password, amount_of_players):
        self.__socket.connect(self.__server_address)
        message = bytes("creating_room", 'utf-8')
        self.__socket.send(message)
        sent_string = room_name + "|_-_|" + str(amount_of_players) + "|_-_|" + password
        message = bytes(sent_string, 'utf-8')
        self.__socket.send(message)
        self.__reset_socket()

    def run(self):
        # Receive/respond loop
        while True:
            print('\nwaiting to receive message')
            data, address = self.__socket.recvfrom(1024)

            print('received {} bytes from {}'.format(
                len(data), address))
            print(data)

            print('sending acknowledgement to', address)
            self.__socket.sendto(b'ack', address)
