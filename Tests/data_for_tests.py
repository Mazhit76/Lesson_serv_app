
import unittest
from dataclasses import dataclass, asdict, astuple, field
from unittest.mock import Mock, call, MagicMock, patch
from Apps.lesson_4_server import Server




@dataclass
class DataTests:
    message: dict[str, str] = field(default_factory=dict)
    value_limits_ip_port: tuple = field(default=(1024, 65535))
    test_ip_address: str = '127.0.0.1'
    test_ip_port: int = 7777


test_message_server_ok = Mock(spec=Server, return_value={'OK': 200})
test_message_server_err = Mock(return_value={'response': 400, 'ERROR': 'Bad request'})
test_message_client_to_server = Mock(return_value={'action': 'presence', 'time': 1635745970.9942236,
                                                   'user': {'account_name': 'Guest'}})

class TestSocket:
    """
    Test class for create tests sockets
    On input test dict off message
    """

    def __init__(self, test_dict):
        self.test_dict = test_dict


