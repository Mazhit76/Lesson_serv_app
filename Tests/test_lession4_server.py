import unittest
from Apps.lesson_4_server import Server
from Apps.utils import ClientServer
from data_for_tests import DataTests



class TestMyCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, 1)

    # def setUp(self):
    #     pass
    #     # self.client_server = ClientServer()
    #     # self.data_test = DataTests()
    #     # self.test_server = Server()
    #
    # def tearDown(self):
    #     pass
    #
    # def setUpModule(self):
    #     pass
    #
    def test_limits_value(self):
        self.assertNotEqual(Server, True)

    def test_dict_CONFIG_ClientServer(self):
        self.client_server = ClientServer()
        self.assertIsInstance(self.client_server.CONFIG, dict, 'CONFIG must is dict')

    def test_dict_CONFIG_is_not_empty(self):
        self.client_server = ClientServer()
        self.assertNotEqual(self.client_server.load_config(), {}, 'Dictionary is empty!!!')

    # def test_CONFIG_default_ip_address(self):
    #     self.client_server = ClientServer()
    #     self.data_test = DataTests()
    #     self.assertEqual(self.client_server.load_config().get('DEFAULT_IP_ADDRESS'), self.data_test.test_ip_address,
    #                      'default ip is not '
    #                      '127.0.0.1')

    # def test_CONFIG_default_port(self):
    #     self.client_server = ClientServer()
    #     self.data_test = DataTests()
    #     self.assertEqual(self.client_server.load_config().get('DEFAULT_IP_PORT'), self.data_test.test_ip_port,
    #                      'Default ip port is not 7777')
    #
    # def test_message_from_client(self):
    #     self.data_test = DataTests()
    #     self.test_server = Server()
    #     self.assertDictEqual(self.test_server.handle_message(self.data_test.test_message_client_to_server),
    #                          self.data_test.test_message_server_ok)
    #
    # def tearDownModule(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
