import threading
import time
from random import randrange


class Worker(threading.Thread):
    _number = None
    _shutdown = False
    _ls = []
    _count = 0
    _mutex = None

    def __init__(self, number: int, ls: list, count: int, mutex: threading.Lock):
        threading.Thread.__init__(self)
        self._ls = ls
        self._number = number
        self._count = count
        self._mutex = mutex

    def run(self) -> None:
        for i in range(self._count):
            self._mutex.acquire()
            self._ls.append(randrange(0, 500))
            self._mutex.release()

    def stop(self):
        self._shutdown = True
        print('Thread ', self._number, ' is Shutdown')


controller = {}
ls = []
lock = threading.Lock()
for i in range(5):
    controller[i] = Worker(number=i, ls=ls, count=1000000, mutex=lock)

for i in controller.keys():
    controller[i].start()

for i in controller.keys():
    controller[i].join()

print(len(ls))