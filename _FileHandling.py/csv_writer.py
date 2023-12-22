import csv
from time import sleep

name = input("What's your name?:")
surname = input("What's your surname?:")
age = input("What's your age:")

with open("Cs50(FileHandling).py/alumni.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, surname, age])