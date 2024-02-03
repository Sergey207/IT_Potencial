import csv

shipNames = []

# Ввод данных
with open('space.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='*')
    for line in reader:
        if line[0] != 'ShipName':
            shipNames.append(line[0])

# Сортировка пузырьком
for i in range(0, len(shipNames) - 1):
    for j in range(0, len(shipNames) - i - 1):
        if int(shipNames[j].split('-')[1]) > int(shipNames[j + 1].split('-')[1]):
            shipNames[j], shipNames[j + 1] = shipNames[j + 1], shipNames[j]

# Вывод
print('\n'.join(shipNames[:10]))
