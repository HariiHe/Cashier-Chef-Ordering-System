import socket
import pickle

#Class in charge of creating the client side of socket communication
#Establish the communication with the server (cooker)
class client(object):
    def __init__(self, master, **kwargs):
        print("3")

    #place your own ip
    def client_socket(self,z):
        s = socket.socket()
        port = 3125
        ip = 'localhost'
        s.connect((ip, port))
        s.sendall(pickle.dumps(z))
        s.close()