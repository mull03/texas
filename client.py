import socket
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


class Reader(threading.Thread):
    def run(self) -> None:
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                return
            print(str(data, "UTF-8"))


start = Reader().start()

while True:
    try:
        s.send(bytearray(input(), "UTF-8"))
    except KeyboardInterrupt:
        break

s.close()