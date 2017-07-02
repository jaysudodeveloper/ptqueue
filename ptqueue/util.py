"""
Utility classes and methods that dont really need to exist in seperate files
"""

import json
import logging
from struct import pack, unpack

LOGGER = logging.getLogger(__name__)

# pylint: disable=C0103
_default_decoder = json.JSONDecoder(object_hook=None, object_pairs_hook=None)
_default_encoder = json.JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    sort_keys=True,
    indent=None,
    separators=None,
    default=None,
)

# pylint: disable=C0111
class CommandMarshaller(object):
    """Wrapper util class for json to marshal queue commands from client"""
    def __init__(self, json_command_object):
        self._json_decoder = _default_decoder
        self._json_encoder = _default_encoder
        self.json_command_object = json_command_object
        self.message_string = None
        self._command_len = None
        self._byte_encoded_message = None
        self._queue_name = ""
        self._action = ""
        self._data = dict()

    def marshal(self):
        try:
            self.message_string = self._json_encoder.encode(self.json_command_object)
        except json.JSONDecodeError as e:
            LOGGER.exception(e)
        self._command_len = len(self.message_string)

        try:
            self._byte_encoded_message = self.message_string.encode("utf-8")
        except UnicodeEncodeError as e:
            LOGGER.exception(e)
        return self._pack_message()

    def unmarshal(self):
        try:
            self.message_string = self.json_command_object.decode("utf-8")
        except UnicodeDecodeError as e:
            LOGGER.exception(e)
        try:
            message_dict = self._json_decoder.decode(self.message_string)
        except json.JSONDecodeError as e:
            LOGGER.exception(e)
        return message_dict

    def _pack_message(self):
        return pack("!I", self._command_len) + self._byte_encoded_message

    def _unpack_message_header(self):
        # struct.unpack("!I", padded_command[:4])[0]
        pass
