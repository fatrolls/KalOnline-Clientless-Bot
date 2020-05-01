import socket
import threading
from .client import Client

class Server():
    def __init__(self):
        # the clients connect to the proxy-server
        self.clients = []

        self.listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listenAddress = ("localhost", 33332)  # "192.168.178.63"
        self.listenSocket.bind(self.listenAddress)
        self.listenSocket.listen(1)             
        self.Run()


    def Run(self):
        """Accept new clients and let them run
        """
        print("Server started on [%s:%s]" % (self.listenAddress))   
        while True:
            gameClientSocket, gameClientAddress = self.listenSocket.accept()
            print("Gameclient connected from [%s:%s]" % (gameClientAddress))
            client = Client(gameClientSocket, gameClientAddress)            
            self.clients.append(client)
