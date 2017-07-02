"""
unittests for ptqueue server
"""

import unittest
from struct import pack, unpack
from ptqueue.util import CommandMarshaller


# pylint: disable=C0111, C0301

class MarshallerTest(unittest.TestCase):
    """Test case for testing marshalling our command objects"""

    def setUp(self):
        self.put_command_bytes = b'{"ARGS": [1], "COMMAND": "PUT", "QUEUE": "test_queue", "KWARGS": {"a": 1}, "TASK": "print"}'
        self.put_command_bytes_h = b'\x00\x00\x00[{"ARGS": [1], "COMMAND": "PUT", "QUEUE": "test_queue", "KWARGS": {"a": 1}, "TASK": "print"}'
        self.put_command_dict = {"COMMAND": "PUT", "QUEUE": "test_queue", "TASK": "print", "ARGS": [1], "KWARGS":{"a": 1}}
        self.get_command_bytes = b'{"COMMAND": "GET", "ID": "40f56719-dbc7-4bc6-96dc-d27bddd21b88"}'
        self.get_command_bytes_h = b'\x00\x00\x00@{"COMMAND": "GET", "ID": "40f56719-dbc7-4bc6-96dc-d27bddd21b88"}'
        self.get_command_dict = {"COMMAND": "GET", "ID": "40f56719-dbc7-4bc6-96dc-d27bddd21b88"}

    def test_marshal_put(self):
        marshaled_result = CommandMarshaller(self.put_command_dict).marshal()
        self.assertIsInstance(marshaled_result, bytes)
        self.assertEqual(len(marshaled_result), len(self.put_command_bytes_h))
        self.assertEqual(sum(marshaled_result), sum(self.put_command_bytes_h))

    def test_unmarshal_put(self):
        unmarshaled_result = CommandMarshaller(self.put_command_bytes).unmarshal()
        self.assertIsInstance(unmarshaled_result, dict)
        self.assertEqual(unmarshaled_result, self.put_command_dict)

    def test_marshal_get(self):
        marshaled_result = CommandMarshaller(self.get_command_dict).marshal()
        self.assertIsInstance(marshaled_result, bytes)
        self.assertEqual(len(marshaled_result), len(self.get_command_bytes_h))
        self.assertEqual(sum(marshaled_result), sum(self.get_command_bytes_h))

    def test_unmarshal_get(self):
        unmarshaled_result = CommandMarshaller(self.get_command_bytes).unmarshal()
        self.assertIsInstance(unmarshaled_result, dict)
        self.assertEqual(unmarshaled_result, self.get_command_dict)

    def test_message_len_header(self):
        message_len_header_bytes_value = pack('!i', len(self.put_command_bytes))
        padded_message = CommandMarshaller(self.put_command_dict).marshal()
        unpadded_message = padded_message[4:]
        message_header = padded_message[:4]
        self.assertIsInstance(message_header, bytes)
        self.assertEqual(message_header, message_len_header_bytes_value)
        self.assertEqual(unpack('!i', message_header), unpack('!i', message_len_header_bytes_value))
        self.assertEqual(len(unpadded_message), len(self.put_command_bytes))
        self.assertEqual(sum(unpadded_message), sum(self.put_command_bytes))

def main():
    """Alias of testcase main method"""
    unittest.main()

if __name__ == '__main__':
    main()
