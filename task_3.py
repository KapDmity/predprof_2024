import csv

"""
Считывание данных из файла в переменную rocket_data
"""

with open("rocket.csv", "r", encoding="utf-8", newline="") as file:
    rocket_data = list(csv.DictReader(file, delimiter=","))

"""
Поиск данных по дате
"""

date = input("Введите дату ")
while date != "sleep":
    for row in rocket_data:
        if row["date"] == date:
            print(f"Шифр: {row['code']} от: {row['rocketparts']} был получен {row['date']}")
            break
    else:
        print("в этот день космос молчал")
    date = input("Введите дату ")
