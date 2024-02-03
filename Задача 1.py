import csv


def check_coords(coords: str) -> bool:
    """
    Checks if 0 in coords - returns False else returns True
    :param coords: str
    :return: bool
    """
    for i in coords.split():
        if int(i) == 0:
            return False
    return True


def fixData(shipName: str, planet: str, direction: str) -> list[str]:
    """
    calculates coords
    :param shipName: str
    :param planet: str
    :param direction: str
    :return: fixed line (list[str])
    """
    shipNumber = shipName.split('-')[1]
    n = int(shipNumber[0])
    m = int(shipNumber[1])
    t = len(planet)
    xd, yd = map(int, direction.split())
    if n > 5:
        x = n + xd
    else:
        x = -(n + xd) * 4 + t
    if m > 3:
        y = m + t + yd
    else:
        y = -(n + yd) * m
    return [shipName, planet, f'{x} {y}', direction]


def main():
    res = open('space_new.txt', mode='w', encoding='utf-8')
    with open('space.txt', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='*')
        for line in reader:
            shipName, planet, coord_place, direction = line
            if shipName != "ShipName" and not check_coords(coord_place):
                line = fixData(shipName, planet, direction)
            print('*'.join(line), file=res)
            if shipName.split("-")[0][-1] == 'V':
                print(f'{shipName} - ({line[-2]})')
    res.close()


main()
