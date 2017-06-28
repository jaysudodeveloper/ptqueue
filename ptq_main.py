import socket
import logging
import ptqueue

"""
"""


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        logging.info("sending: %s", message)
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    HOST, PORT = "localhost", 6000

    server = ptqueue.server.PtQueueServer((HOST, PORT), ptqueue.server.JsonCommandHandler)
    ip, port = server.server_address

    LOGGER.info("server started on %s %d", ip, port)
    server.serve_forever()