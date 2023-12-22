# Sorting by specific value in file
# csv module usage
# Initialize empty list
from time import sleep
from csv import reader
students = []

with open("Cs50(FileHandling).py/students.csv") as file:
    #reader variable holds the reader object that reads the content of the csv file
   reader = reader(file)
   #iterate through the rows in reader variable(csv file)
   for fname, sname, gender, year in reader:
       #append dictionary into list(.lower changes gender values to lowercase)
       student = {"fname":fname, "sname":sname, "gender":gender.lower(), "year":year}
       students.append(student)
        
# def get_sname(student):
#     return student["sname"]

#for each student in students list..(sorted sorts the values in ascending order and the key takes a lambda function specifying fname as the order of sorting)       
for student in sorted(students, key= lambda student: student["fname"]):
    #halt output
    sleep(2)
    #print string
    print (f"{student['fname']} {student['sname']} is a {student['gender']} in {student['year']}.")