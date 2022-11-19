import unittest
from account import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def tearDown(self):
        del self.a1
        del self.a2

    def test_init(self):
        self.assertEqual(self.a1.get_name(), 'John')
        self.assertEqual(self.a1.get_balance(), 0)
        self.assertEqual(self.a2.get_name(), 'Jane')
        self.assertEqual(self.a2.get_balance(), 0)

    def test_deposit(self):
        self.a1.deposit(20.50)
        self.assertEqual(self.a1.__str__(), 'Name = John, Balance = 20.50')
        self.assertEqual(self.a2.__str__(), 'Name = Jane, Balance = 0')

    def test_withdraw(self):
        self.a1.__account_balance = 20
        self.a1.withdraw(11.25)
        self.assertEqual(self.a1.__str__(), 'Name = John, Balance = 8.75')