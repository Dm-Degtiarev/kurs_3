from utils import arrs
from main import main


def test_reformat_acc_number():
    assert arrs.reformat_acc_number("Скрытый счет ") == 'Скрытый счет '
    assert arrs.reformat_acc_number("26922265121") == 'Счет **5121 '



