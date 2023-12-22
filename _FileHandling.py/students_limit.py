# There is only space for 7 students in SS2. Exit the program if an attempt is made to input an eighth student
from time import sleep
student = input("Enter SS2 student name: ")
with open("Cs50(FileHandling).py/students.txt", "r") as file:
    #readlines method reads lines from the file and returns a list of students. Len returns the number of students in the list.
    if len(file.readlines()) >= 7:
        print ("No more students allowed in SS2.")
        sleep(1)
        with open("Cs50(FileHandling).py/rejected_students.txt", "a") as file2:
             file2.write(f"{student}\n")
        SystemExit()
    else:
        with open("Cs50(FileHandling).py/students.txt", "a") as file3:
            file3.write(f"{student}\n")