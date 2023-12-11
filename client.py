import socket
import sys
import select
import threading
from constants import HEADER, PORT, SERVER,  ADDR, FORMAT, DISCONNECT_MESSAGE

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
  send_length = str(msg_length).encode(FORMAT)
  send_length += b' ' * (HEADER - len(send_length))
  server.send(send_length)
  server.send(message)

conn = True
while conn:
  # sys.stdin - is you inputting
  # server
    sockets_list = [sys.stdin, server]
    read_sockets,_, _ =select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            message = message.decode()
            print(message)
        else:
            message = input()
            if message == "exit":
              conn = False
            send(message)

send(DISCONNECT_MESSAGE)
server.close()