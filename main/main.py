from utils.arrs import *


def main(oper_cnt=5):
    """
    Выводит в консоль информацию по
    заданному кол-ву успешных транзакций
    (по умолчанию - 5шт)
    """
    operations = dicts_open_and_sort('date')
    for operation in operations:
        if oper_cnt == 0:
            break
        elif operation['state'] == 'EXECUTED':
            oper_cnt -= 1
            oper_date = reformat_date(operation['date'])
            oper_desc = operation['description']
            sum_money = f"{operation['operationAmount']['amount']} \
{operation['operationAmount']['currency']['name']}"

            if 'счет' in operation['from'].lower():
                sender = reformat_acc_number(operation['from'])
            else:
                sender = reformat_card_number(operation['from'])
            if 'счет' in operation['to'].lower():
                recipient = reformat_acc_number(operation['to'])
            else:
                recipient = reformat_card_number(operation['to'])

            print(f"{oper_date} {oper_desc}\n{sender}-> {recipient}\n{sum_money}\n")


if __name__ == '__main__':
    main()