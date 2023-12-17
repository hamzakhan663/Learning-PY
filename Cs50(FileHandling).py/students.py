# student = input("Enter SS2 student name: ")
# with open("Cs50(FileHandling).py/students.txt", "a") as file:
#     file.write(f"{student}\n")
# # file.close()
from time import sleep
with open("Cs50(FileHandling).py/students.txt", "r") as file:
    lines = file.readlines()

print(f"Students in SS2 are: ")
 
for line in lines:
    sleep(2)
    print(line, end = "")