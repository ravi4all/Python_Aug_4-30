import csv

path = "data.csv"

data = ["First Name, Last Name".split(","),
        "Sachin, Tendulkar".split(","),
        "MS, Dhoni".split(","),
        "John, Cena".split(","),
        "Virat,Kohli".split(",")]

with open(path, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for line in data:
        writer.writerow(line)
