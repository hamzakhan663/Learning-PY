import csv

name = input("What's the name of the film: ")
genre = input("What type of film is it: ")
file_path = "Cs50(FileHandling).py/film_list.csv"

with open(file_path, 'a', newline= '') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "genre"])
    writer.writerow({"name": name, "genre": genre})