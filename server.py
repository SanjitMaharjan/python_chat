import socket
import threading

from constants import HEADER, PORT, SERVER,  ADDR, FORMAT, DISCONNECT_MESSAGE

# threading is a way of creting multiple threads on one python program

# import time
# time.sleep(1)
# print("HELLO")



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET = ipv4  what types of ip address are we looking for
# SOCK STREAM - way of sending data
server.bind(ADDR)
clients = []  

def handle_client(conn, addr):
  """handle all the communication from the server and client"""
  print(f"[NEW_CONNECTION] {addr} connected")
  
  connected = True
  while connected:
    # try:
      msg_length = conn.recv(HEADER).decode(FORMAT) # blocking lines
      if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
          connected = False
        print(f"[{addr}] {msg}")
        for connection in clients:
          try:
            if connection == conn:
              connection.send(f"<YOU> {msg}".encode(FORMAT))
            else:
              connection.send(f"<{addr[0]}> {msg}".encode(FORMAT))
          except OSError:
            if connection == conn:
              connection.send(f"<YOU> Invalid Message.".encode(FORMAT))
            else:
              connection.send(f"<{addr[0]}> Invalid Message".encode(FORMAT))
          except BrokenPipeError:
            pass
    # except ConnectionResetError:
    #   connected = False
  
  conn.close()
  

def start():
  """code to allow our server to start listening for connections and then handling those connections and passings them to handle clients which will run in a new thread"""
  server.listen()
  print(f"[LISTENING] Server is listening on {SERVER}")
  while True:
    conn, addr = server.accept() # store the connection, addr means address (from where does it come from) # blocking lines
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    clients.append(conn)
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting....")
start()
