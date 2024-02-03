import csv

res = []


def generate_password(shipName: str, planet: str) -> str:
    """
    Returns password by data
    :param shipName: name of the ship
    :param planet: name of the planet
    :return: generated password
    """
    return f'{planet[-3:]}{shipName[2:0:-1]}{planet[2::-1]}'.upper()


# Ввод данных
with open('space.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='*')
    for line in reader:
        if line[0] == 'ShipName':
            res.append(line + ['password'])
        else:
            res.append(line + [generate_password(*line[:2])])

# Вывод данных в файл space_uniq_password.csv
with open('space_uniq_password.csv', mode='w', encoding='utf-8') as f:
    for line in res:
        print('*'.join(line), file=f)
