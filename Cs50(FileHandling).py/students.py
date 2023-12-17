# student = input("Enter SS2 student name: ")
# with open("Cs50(FileHandling).py/students.txt", "a") as file:
#     file.write(f"{student}\n")
# # file.close()


from time import sleep
# with open("Cs50(FileHandling).py/students.txt", "r") as file:
#     print(f"Students in SS2 are: ")
#     for line in sorted(file):
#         sleep(2)
#         print(line, end = "")


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



# There is only space for 7 students in SS2. Exit the program if an attempt is made to input an eighth student
student = input("Enter SS2 student name: ")
with open("Cs50(FileHandling).py/students.txt", "r") as file:
    #readlines method reads lines from the file and returns a list of students. Len returns the number of students in the list.
    if len(file.readlines()) > 7:
        print ("No more students allowed in SS2.")
        sleep(1)
        with open("Cs50(FileHandling).py/rejected_students.txt", "a") as file2:
             file2.write(f"{student}\n")
        SystemExit()
    else:
        with open("Cs50(FileHandling).py/students.txt", "a") as file3:
            file3.write(f"{student}\n")