"""
Python task queue server
"""
import logging
import socketserver
from .util import CommandMarshaller

# pylint: disable=C0111

LOGGER = logging.getLogger(__name__)


class JsonCommandHandler(socketserver.BaseRequestHandler):
    """Handles json formatted commands"""

    def __init__(self):
        super().__init__()
        self.msg_len = ""
        self.message = ""

    def setup(self):
        # TODO: implement marshalling in setup method after writing tests
        pass

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        # print(data)
        LOGGER.info("received form client: %s", data)

class PtQueueServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Threaded version of socketserver TCPServer"""
    pass
