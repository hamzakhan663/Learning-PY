# Sorting by specific value in file

# Initialize empty list
from time import sleep
students = []

with open("Cs50(FileHandling).py/students.csv") as file:
    for line in file:
        fname, sname, gender, year = line.rstrip().split(",")
        student = {"fname":fname, "sname":sname, "gender":gender.lower(), "year":year}
        students.append(student)
        
# def get_sname(student):
#     return student["sname"]
        
for student in sorted(students, key= lambda student: student["fname"]):
    sleep(2)
    print (f"{student['fname']} {student['sname']} is a {student['gender']} in {student['year']}.")