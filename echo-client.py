import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user_input = input()
    s.sendall(bytes(user_input, encoding='utf-8'))
    data = s.recv(1024)

print('received', repr(data))
