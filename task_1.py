import csv

"""
Считывание данных из файла в переменную data
"""

with open('rocket.csv', 'r', encoding="utf-8", newline="") as file:
    data = list(csv.reader(file, delimiter=","))[1:]

"""
Запись мксяцев и количества шифров для каждого месяца в словарь data_new
"""

data_new = {}
for row in data:
    if row[0].split("-")[1] in data_new:
        data_new[(row[0].split("-")[1])] += 1
    else:
        data_new[row[0].split("-")[1]] = 1

data_months = []
for row in data_new:
    data_months.append(f"В {row} было получено - {data_new[row]} шифров")

"""
Запись данных в новый файл "rocket_part.txt "
"""

with open("rocket_part.txt ", "w", newline="", encoding="utf-8") as new_file:
    for row in data_months:
        new_file.write(f"{row}\n")

"""
Вывод необходимой информации для выбранного месяца
"""

with open("rocket_part.txt", "r", encoding="utf-8") as f1:
    mon = input("Введите номер месяца ")
    f = f1.readlines()
    for row in f:
        if mon in row[2:4]:
            print(row)
