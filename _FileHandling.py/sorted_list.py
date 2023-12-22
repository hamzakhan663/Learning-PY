from time import sleep
with open("Cs50(FileHandling).py/students.txt", "r") as file:
    print(f"Students in SS2 are: ")
    for line in sorted(file):
        sleep(2)
        print(line, end = "")

