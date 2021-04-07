# Server side python file

# ~/PycharmProjects/HW3

import socket
from _ast import While

HOST = '127.0.0.1' # localhost - standard loopback interface address
PORT = 65432       # Port to listen on non-privileged ports are > 1023

# User the socket object without calling s.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
