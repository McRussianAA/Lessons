import socket
from ExampleSocket.Worker import WorkerSocket
import random

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7777))
server.listen()


def CloseWorker(id: int):
    print('Worker ', id, ' Closed')


while True:
    sock, addr = server.accept()
    print('Connection from ', addr)
    worker = WorkerSocket.WorkerSocket(sock=sock, id=random.randrange(1, 1000),
                                       callback=CloseWorker)
    worker.start()

print('Socket stop')
