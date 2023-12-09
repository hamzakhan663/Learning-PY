class Student:
    hands = 2
    mouth = 1
    legs = 2
    def __init__(self,name,age,gender,registration_number,course):
        self.name = name
        self.age = age
        self.gender = gender
        self.registration_number = registration_number
        self.course = course
        self.exam_score = None
    
    def takeExam(self):
        score = float(input("Enter your Exam Score: "))
        self.exam_score = score
        print(f"{self.name} scored {score}")
        


    
        
        
Student1 = Student("Hamza", 18, "male", "AEO9098", "ADSE")
Student2 = Student("Ben", 18, "male", "AEO9099", "ADSE")
Student3 = Student("Aisha", 19, "female", "AEO9100", "ADSE")

Student1.takeExam()
# Student2.takeExam()
# Student3.takeExam()
        
print(f"I am {Student1.name}, an {Student1.age} year old {Student1.gender}. I hold number {Student1.registration_number} of this institution and my course is {Student1.course}")