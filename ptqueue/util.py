"""
Utility classes and methods that dont really need to exist in seperate files
"""

import json
import collections
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
        self._command = ""
        self._queue_name = ""
        self._action = ""
        self._data = dict()

    def marshal(self):
        command_string = self._json_encoder.encode(self.json_command_object)
        return command_string.encode("utf-8")

    def unmarshal(self):
        command_string = self.json_command_object.decode("utf-8")
        return self._json_decoder.decode(command_string)
