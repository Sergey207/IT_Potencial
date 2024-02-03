import csv

ships = []


def getName(ship_name: str) -> str:
    """
    This function returns formatted info about ship
    :param ship_name: str
    :return: formatted string
    """
    for i in ships:
        if i[0] == ship_name:
            return f"Корабль {i[0]} был отправлен с планеты: {i[1]} и его направление движения было: {i[2]}"
    return "error.. er.. ror.."


# Ввод данных
with open('space.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='*')
    for line in reader:
        if line[0] != 'ShipName':
            ships.append([line[0], line[1], line[3]])

# Бесконечный ввод
run = True
while run:
    ui = input()
    if ui == 'stop':
        run = False
    else:
        print(getName(ui))
