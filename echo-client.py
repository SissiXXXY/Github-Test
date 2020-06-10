import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    def sendmsg():
        while True:
            user_input = input()
            if user_input != 'finish':
                s.sendall(user_input.encode('utf-8'))
            else:
                break


    def getrps():
        data = s.recv(1024)
        print('received', data.decode("utf-8"))

thread_sendmsg = threading.Thread(target=sendmsg(), args=())
thread_getrps = threading.Thread(target=getrps(), args=())
p = [thread_sendmsg, thread_getrps]
for i in range(len(p)):
    p[i].start()
for i in range(len(p)):
    p[i].join()
