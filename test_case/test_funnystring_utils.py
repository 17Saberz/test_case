from funnystring.funnystring_utils import is_funny_string
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_ivvkxq_is_funny(self):
        funny_string = 'ivvkxq'
        is_funny = is_funny_string(funny_string)
        self.assertEqual(is_funny, 'Not Funny')
    # def test_give_1_2_3_is_prime(self):
    #     prime_list = [1, 2, 3]
    #     is_prime = is_prime_list(prime_list)
    #     self.assertTrue(is_prime)