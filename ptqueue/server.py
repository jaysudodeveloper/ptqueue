"""
Python task queue server
"""
import logging
import socketserver
import json

# pylint: disable=C0111

LOGGER = logging.getLogger(__name__)


class JsonCommandHandler(socketserver.BaseRequestHandler):
    """Handles json formatted commands"""

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        # print(data)
        LOGGER.info("received form client: %s", data)

class PtQueueServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Threaded version of socketserver TCPServer"""
    pass
