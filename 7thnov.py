# PASSING A CLASS INTO ANOTHER CLASS

class Student:
    
    def __init__(self,name,age,student_number):
        self.name = name
        self.age = age
        self.student_number = student_number
        self.max_courses = 3
        self.courses_registered = []
        
    def add_courses(self,course):
        if len(self.courses_registered) < self.max_courses:
            self.courses_registered.append(course)
            print("Course has been added for student")
        else:
            print("Course could not be added for student")
        
    def __str__(self):
        return self.name
        
  
class Course:
    
    def __init__(self,name,units,max_students):
        self.name = name
        self.units = units
        self.max_students = max_students
        self.student_list = []
        
    def register_student(self,student):
        if len(self.student_list) < self.max_students:
            self.student_list.append(student)
            student.add_courses(self)
            print("Student added succesfully")
        else:
            print("Student registration failed")
    
    
    def __str__(self):
        return self.name
    
        

student_1 = Student("Mark",18,"004")
student_2 = Student("Chelsea",20,"007")
student_3 = Student("Godswill",19,"003")
student_4 = Student("Favour",29,"001")

course_1 = Course("Python",4,3)

course_1.register_student(student_1)
# course_1.register_student(student_2)
# course_1.register_student(student_3)

print(course_1.student_list[0])

print(student_1.courses_registered[0])