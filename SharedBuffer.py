import threading

class SharedBuffer:
    '''
    Объект этого класса представляет собой небольшой буфер (очередь),
    который будет разделяться между VideoStream и Worker's.
    Буфер имеет ограниченный размер
    VideoStream будет класть в буфер кадры, а Worker' - их забирать.
    Все воркеры должы получать один и тот же кадр, и толкьо после этого
    переключаться на получение более свежего...
    '''

    _mutex = None
    _max_count = 0
    _buffer = None

    def __init__(self, count: int):
        self._mutex = threading.Lock()
        self._max_count = count
        self._buffer = []

    def push(self, data):
        self._mutex.acquire()
        self._buffer.append(data)
        if len(self._buffer) > self._max_count:
            self._buffer.pop(0)
        self._mutex.release()

    def pop(self):
        self._mutex.acquire()
        if len(self._buffer) == 0:
            self._mutex.release()
            raise Exception()

        data = self._buffer.pop()
        self._mutex.release()

        return data

    def __len__(self):
        self._mutex.acquire()
        l = len(self._buffer)
        self._mutex.release()
        return l