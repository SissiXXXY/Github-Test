import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        user_input = input()
        if user_input != 'finish':
            s.sendall(user_input.encode('utf-8'))
        else:
            break
        data = s.recv(1024)
        print('received', data.decode("utf-8"))
