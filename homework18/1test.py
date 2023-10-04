import unittest
from unittest.mock import Mock
from bank_classes import SavingsAccount, Bank


class TestBank(unittest.TestCase):
    def test_open_account(self):
        bank = Mock(spec=Bank)
        account = Mock(spec=SavingsAccount)
        account.get_balance.return_value = 0
        bank.open_account(account)
        bank.open_account.assert_called_once_with(account)
        self.assertEqual(account.get_balance(), 0)


unittest.main()
