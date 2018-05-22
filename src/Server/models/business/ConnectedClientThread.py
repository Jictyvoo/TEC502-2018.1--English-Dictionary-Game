import threading


class ConnectedClientThread(threading.Thread):
    def __init__(self, client_connection, client_address):
        threading.Thread.__init__(self)
        self.__clientConnection = client_connection
        self.__clientAddress = client_address

    def run(self):
        print("Kappa")
