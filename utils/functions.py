import json
from datetime import datetime

def load_operations(path):
    with open(f'{path}', encoding="utf-8") as data:
        return json.load(data)


def checkout(path = '../operations.json'):
    '''Function which gives you the
    list of id of 5 last executed operations'''
    operations_data = load_operations(path)
    timelist = []
    checkeddata = []
    doublechecked = []
    for i in operations_data:
        if i != {} and i['state'] == "EXECUTED":
            datetime_str = i['date']
            timelist.append(datetime_str)
    timelist.sort()
    for item in timelist[-5:]:
        checkeddata.append(item)
    for item in operations_data:
        if item != {} and item['date'] in checkeddata:
            doublechecked.append(item['id'])
    return doublechecked


def censored(card1, path = '../operations.json'):
    '''Function which makes card details not visible'''
    operations_data = load_operations(path)
    if card1 is None:
        return 'Данные отсутствуют'
    card1 = card1.split()
    uncensored_part = " ".join(card1[:-1])
    if 'Счет' in uncensored_part:
        card1[-1] = card1[-1].replace(card1[-1][:-4], '*' * len(card1[-1][:-4]))
        censored_part1 = "".join(card1[-1][-6:])
    else:
        card1[-1] = card1[-1].replace(card1[-1][6:-4], '*' * len(card1[-1][6:-4]))
        censored_part1 = " ".join([card1[-1][i:i+4] for i in range(0, len(card1[-1]), 4)])
    finale_censored = " ".join([uncensored_part, censored_part1])
    return finale_censored


def last_struggle(path = '../operations.json'):
    '''Function which prints the details
    about the last 5 operations'''
    operations_data = load_operations(path)
    checked = checkout(path)
    for item in operations_data:
        if item != {} and item['id'] in checked:
            if item['description'] == "Открытие вклада":
                card1 = None
            else:
                card1 = item['from']
            card2 = item['to']
            datetime_str = item['date']
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f')
            print(f"{datetime_obj.date().strftime('%d.%m.%Y')} {item['description']}")
            print(f"{censored(card1, path)} ==> {censored(card2, path)}")
            print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
