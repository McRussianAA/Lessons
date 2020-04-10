from unittest import TestCase
from tools import CheckValidMail

class TestCheckValidMail(TestCase):
    def test_CheckValidMail(self):
        self.assertTrue(CheckValidMail('login@hotmail.com'))
        self.assertTrue(CheckValidMail('user.user@mail.hotmail.com'))
        self.assertFalse(CheckValidMail('login.hotmail.com'))
        self.assertFalse(CheckValidMail('login@hotmail@com'))
        self.assertFalse(CheckValidMail('.@hotmail.com'))
        self.assertFalse(CheckValidMail('login.@hotmail..com'))
        self.assertFalse(CheckValidMail('logi n@hot mail.com'))
        self.assertTrue(CheckValidMail('   login@hotmail.com   '))

    def test_RaiseException(self):
        self.assertRaises(TypeError, CheckValidMail, (12))
        self.assertRaises(TypeError, CheckValidMail, (2.7))
        self.assertRaises(TypeError, CheckValidMail, ([1, 3]))