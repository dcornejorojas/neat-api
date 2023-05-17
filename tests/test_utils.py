import unittest
import os

from src.utils import Utils

class Test_Utils(unittest.TestCase):
    def test_get_secret_should_return_empty_secret_when_secret_not_exist(self):
        utils = Utils()
        key = 'secretKey'
        type = 'secret'
        actual_response = utils.get_secret(key, type)
        expected_response = ''
        self.assertEqual(actual_response, expected_response)
    
    def test_get_secret_should_return_env_var_when_type_is_env(self):
        utils = Utils()
        key = 'secretKey'
        os.environ[key] = 'actualValueEnv'
        actual_response = utils.get_secret(key)
        expected_response = 'actualValueEnv'
        self.assertEqual(actual_response, expected_response)