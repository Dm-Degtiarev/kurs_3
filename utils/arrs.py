import json
from re import sub
from datetime import datetime


def dicts_validation(checked_dict):
    """
    Проверяет корректность вложенных словарей
    если ключ date не найден - удаляет словарь
    если не найден ключ from - создает его со
    значение: "Скрытый счет"
    """
    for oper_dict in checked_dict:
        try:
            oper_dict['date']
            oper_dict['from']
        except KeyError as ex_attr:
            fail_index = checked_dict.index(oper_dict)
            if str(ex_attr) == "'date'":
                del checked_dict[fail_index]
            elif str(ex_attr) == "'from'":
                checked_dict[fail_index]['from'] = "Скрытый счет "
            else:
                print(f"Error: index: {fail_index}, key: {ex_attr}")

    return checked_dict


def dicts_open_and_sort(sort_attr, json_file='operations.json'):
    """
    Открывает Json указанный в параметре 'json_file', а так же
    сортирует список словарей по заданному атрибуту словаря
    """
    with open(json_file, 'r', encoding='utf8') as operations:
        operations = json.load(operations)
        operations = dicts_validation(operations)
        operations.sort(key=lambda sort: sort[sort_attr], reverse=True)

    return operations


def reformat_card_number(inp_card):
    """
    Приводит введенный номер карты к формату:
    "Назваине карты" XXXX XX** **** XXXX
    """
    card_name = inp_card[-18::-1][::-1]
    card_num = (inp_card[-1:-5:-1] + "******" + inp_card[-11:-17:-1])[::-1]
    card_num_new_f = sub("([^ ]{4})", r"\1 ", card_num)
    new_format = f"{card_name} {card_num_new_f}"

    return new_format


def reformat_acc_number(inp_acc):
    """
    Приводит введенный номер счета к формату:
    '**XXXX'
    """
    if inp_acc == 'Скрытый счет ':
        pass
    else:
        inp_acc = f"Счет **{inp_acc[-1:-5:-1][::-1]} "

    return inp_acc


def reformat_date(inp_date):
    """
    Форматирует дату из 'Y-%m-%dT%H:%M:%S.%f'
    в '%d.%m.%Y'
    """
    new_date_f = datetime.strptime(inp_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date_f = new_date_f.strftime("%d.%m.%Y")

    return new_date_f