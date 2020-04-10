import socket
import struct

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 7777))

for _ in range(10):
    msg = 'Hello World!'.encode()
    head = struct.pack('II12s', len(msg), 0, '            '.encode())
    sock.sendall(head)
    sock.sendall(msg)

    head = sock.recv(20)
    size, code, inf = struct.unpack('II12s', head)
    msg = sock.recv(size)
    print(msg.decode())
