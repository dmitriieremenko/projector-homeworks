import unittest
from unittest.mock import Mock, patch
from bank_classes import SavingsAccount, CurrentAccount, Bank


class TestBank(unittest.TestCase):
    def test_update(self):
        bank = Bank()
        saving_account = Mock(spec=SavingsAccount)
        current_account = Mock(spec=CurrentAccount)
        bank.open_account(saving_account)
        bank.open_account(current_account)
        bank.update()
        saving_account.add_interest.assert_called_once()
        current_account.send_letter.assert_called_once()

        with patch('builtins.print') as mock_print:
            current_account.send_letter.assert_called_once()
            mock_print.assert_called_once()


unittest.main()
