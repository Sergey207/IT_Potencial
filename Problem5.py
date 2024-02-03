import csv


def shipByPlanet(planet_name: str) -> list[str]:
    """
    Returns names of ships that started from the given planet
    :param planet_name: name of planet
    :return: list of names of ships
    """
    return ships[planet_name]


ships = dict()

# Ввод данных
with open('space.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='*')
    for line in reader:
        if line[0] != 'ShipName':
            if line[1] in ships:
                ships[line[1]].append(line[0])
            else:
                ships[line[1]] = [line[0]]

# Вывод данных
length = 0
for k, v in ships.items():
    if length == 10:
        break
    for s in v:
        print(f'{k}: {s}')
        length += 1
