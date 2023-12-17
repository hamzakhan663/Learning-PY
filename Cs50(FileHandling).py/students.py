# student = input("Enter SS2 student name: ")
# with open("Cs50(FileHandling).py/students.txt", "a") as file:
#     file.write(f"{student}\n")
# # file.close()
from time import sleep
with open("Cs50(FileHandling).py/students.txt", "r") as file:
    print(f"Students in SS2 are: ")
    for line in sorted(file):
        sleep(2)
        print(line, end = "")


#Sorted list of students


#Initialize empty list
# students = []

# #read is default for open
# with open("Cs50(FileHandling).py/students.txt") as file:
#     #for one line in the opened file..
#     for line in file:
#         #insert the names in the file into students list
#         students.append(line)

# #for one student in the sorted list
# print(f"Students in SS2 are:")    
# for student in sorted(students):
#     sleep(2)
#     #print the students list but sorted
#     print(student, end = "")