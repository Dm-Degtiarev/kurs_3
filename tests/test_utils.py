from utils import arrs
from main import main


def test_reformat_acc_number():
    assert arrs.reformat_acc_number("Скрытый счет ") == 'Скрытый счет '
    assert arrs.reformat_acc_number("26922265121") == 'Счет **5121 '


def test_dicts_validation():
    assert arrs.dicts_validation([{'date': "2019-08-26T10:50:58.294041"}])\
           == [{'date': '2019-08-26T10:50:58.294041', 'from': 'Скрытый счет '}]
    assert arrs.dicts_validation([{'date': "2019-08-26T10:50:58.294041", 'from': '5555555'}])\
           == [{'date': "2019-08-26T10:50:58.294041", 'from': '5555555'}]
    assert arrs.dicts_validation([{}]) == []


def test_dicts_open_and_sort():
    assert arrs.dicts_open_and_sort('date', json_file='test_item.json') ==\
           [{'date': '2025-06-08', 'from': 'Скрытый счет '},
            {'date': '2025-05-03', 'from': 'Скрытый счет '},
            {'date': '1990-01-25', 'from': 'Скрытый счет '}]


def test_reformat_card_number():
    assert arrs.reformat_card_number('Лучшая карта 1558698725362517') ==\
        'Лучшая карта 1558 69** **** 2517 '


def test_reformat_date():
    assert arrs.reformat_date('2019-07-03T18:35:29.512364') == '03.07.2019'


def test_main():
    assert main.main(operations_path='test_operations.json') == None
