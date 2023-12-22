# Sorting by specific value in file


from time import sleep #import sleep function
students = [] # Initialize empty list

#open csv file
with open("Cs50(FileHandling).py/students.csv") as file:
    #iterate through the lines in the file(). Unpacks list of strings gotten from split(which divides the values based on the commas). Each var is a column in the csv file. Create dictionaries to store the information of the students
    for line in file:
        fname, sname, gender, year = line.rstrip().split(",")
        student = {"fname":fname, "sname":sname, "gender":gender.lower(), "year":year}
        #append the dictionaries to the list
        students.append(student)

#function that can be otherwise done using lambda       
# def get_fname(student):
#     return student["fname"]


#for each student in students list..(sorted sorts the values in ascending order and the key takes a lambda function specifying fname as the order of sorting)        
for student in sorted(students, key= lambda student: student["fname"]):
    sleep(2)
    print (f"{student['fname']} {student['sname']} is a {student['gender']} in {student['year']}.")