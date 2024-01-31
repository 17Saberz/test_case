from alterchar.alterchar_utils import alternatingCharacters
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_BBABAAAABB_is_5(self):
        string = 'BBABAAAABB'
        deletions = alternatingCharacters(string)
        self.assertEqual(deletions, 5)

    def test_give_AAABBBAABB_is_6(self):
        string = 'AAABBBAABB'
        deletions = alternatingCharacters(string)
        self.assertEqual(deletions, 6)

    