import csv


def command_create(date, code, rocketparts):
    words = list(rocketparts.split())
    firstPart = ""
    for i in words:
        firstPart += i[0].upper()

    kirilic = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЯЧСМИТЬБЮЁ"
    latin = "QWERTYUIOPASDFGHJKLZXCVBNM"
    d = ""
    l = ""
    k = ""
    for i in code:
        if i.isdigit() == True:
            d += i
        elif i in latin:
            l += i
        elif i in kirilic:
            k += i
    new_code = d + l + k

    new_date = str(2024 - int(date[:4]))

    return str(firstPart + " " + new_code + " " + new_date)


"""
Считывание данных из файла в переменную data
"""

with open('rocket.csv', 'r', encoding="utf-8", newline="") as file:
    data = list(csv.reader(file, delimiter=","))[1:]

for i in range(len(data)):
    data[i].append(command_create(data[i][0], data[i][1], data[i][2]))

with open("rocket_commands.csv", "w", newline="", encoding="utf-8") as new_file:
    writer = csv.writer(new_file)
    n = ["date", "code", "rocketparts"]
    writer.writerow(n)
    writer.writerows(data)
