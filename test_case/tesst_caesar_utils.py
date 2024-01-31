from caesar.caesar_utils import caesarCipher
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_Hello_World_and_4_is_Lipps_Asvph(self):
        string = 'Hello_World'
        number = 4
        encrypted = caesarCipher(string, number)
        self.assertEqual(encrypted, 'Lipps_Asvph')