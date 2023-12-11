import socket

HEADER = 64  # length of amount of bytes of message
PORT = 5058 # using port not being used for something else
IPADDRESS = socket.gethostname() # server ip address (this is my ip address) localhost ip
IPADDRESS = "192.168.1.72" # server ip address (this is my ip address)
SERVER = socket.gethostbyname(IPADDRESS)  # get my ip address automiatically
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Bye bye"


