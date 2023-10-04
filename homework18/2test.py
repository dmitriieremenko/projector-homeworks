import unittest
from unittest.mock import Mock, patch
from bank_classes import SavingsAccount, CurrentAccount, Bank
from io import StringIO


class TestBank(unittest.TestCase):
    def test_update(self):
        bank = Bank()
        saving_account = Mock(spec=SavingsAccount)
        current_account = Mock(spec=CurrentAccount)
        bank.open_account(saving_account)
        bank.open_account(current_account)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            bank.update()
            saving_account.add_interest.assert_called_once()
            current_account.send_letter.assert_called_once()
        output = mock_stdout.getvalue().strip()
        expected_output = ''
        self.assertEqual(output, expected_output)


unittest.main()
