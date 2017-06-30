"""
Utility classes and methods that dont really need to exist in seperate files
"""

from decoder import JSONDecoder
from encoder import JSONEncoder

# pylint: disable=C0103
_default_decoder = JSONDecoder(object_hook=None, object_pairs_hook=None)
_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
)

# pylint: disable=C0111
class CommandMarshaller(object):
    """Wrapper util class for json to marshal queue commands from client"""
    def __init__(self, json_command):
        self._decoder = _default_decoder
        self._encoder = _default_encoder
        self.json_command = json_command
        self._command = ""
        self._queue_name = ""
        self._action = ""
        self._data = dict()

    def marshal(self):
        pass

    def unmarshal(self):
        pass

    @property
    def command(self):
        pass

    @property
    def queue(self):
        pass

    @property
    def action(self):
        pass

    @property
    def arg_data(self):
        pass

    @property
    def kwarg_data(self):
        pass
