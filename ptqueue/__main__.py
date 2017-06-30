"""
executable
"""
import os
import socket
import logging
from .server import JsonCommandHandler, PtQueueServer



LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        logging.info("sending: %s", message)
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    HOST, PORT = "localhost", 6000

    SERVER = PtQueueServer((HOST, PORT), JsonCommandHandler)

    LOGGER.info("server started on %s %d", HOST, PORT)

    SERVER.serve_forever()
