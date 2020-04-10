import socket
import threading
import struct


class WorkerSocket(threading.Thread):
    _sock = None
    _id = None
    _callback = None

    def __init__(self, sock: socket.socket, id: int, callback):
        threading.Thread.__init__(self)
        self._sock = sock
        self._callback = callback
        self._id = id

    def run(self) -> None:
        while True:
            try:
                head = self._GetRawDataFromSocket(size=20)
            except Exception:
                break
            size, code = self._ParseHead(data=head)
            try:
                msg = self._GetRawDataFromSocket(size=size)
                print(code, msg)
            except Exception:
                break
            msg = self._CreateMessage(code=code)
            head = self._CreateHeadForMessages(msg=msg, code=code)
            try:
                self._SendRawDataToSocket(head)
            except Exception:
                break
            try:
                self._SendRawDataToSocket(msg)
            except Exception:
                break
        self._callback(self._id)
        print('Socket Closed')

    def _GetRawDataFromSocket(self, size: int) -> bytes:
        data = self._sock.recv(size)
        if not data:
            raise Exception()
        total_recv = len(data)
        while total_recv != size:
            current = self._sock.recv(size - total_recv)
            data = data + current
            total_recv += len(current)
        return data

    def _SendRawDataToSocket(self, msg: bytes):
        total_send_bytes = len(msg)
        current_send_bytes = self._sock.send(msg)
        while current_send_bytes != total_send_bytes:
            current_send_bytes += self._sock.send(msg[current_send_bytes: ])

    def _ParseHead(self, data: bytes) -> tuple:
        size, code, inf = struct.unpack('II12s', data)
        return size, code

    def _CreateMessage(self, code: int) -> bytes:
        rez = 'Operation ' + str(code) + ' Complete!!!'
        return rez.encode()

    def _CreateHeadForMessages(self, msg: str, code: int) -> bytes:
        head = struct.pack('II12s', len(msg), code, 'ssssssssssss'.encode())
        return head