import socket

class UDPReceiver:
    def __init__(self, ip="0.0.0.0", port=20777, buffer_size=2048):
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
    def packets(self):
        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            yield data
    def close(self):
        self.sock.close()