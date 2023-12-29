class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Provide a name")
        self.name = name
        self._house = house
       

    def __str__(self):
        return f" Hi, {self.name}. Welcome to your house, {self.house}."
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
         self._house = house

def main():
    student = get_students()
    # student.house = "Kingdom of Redania"
    print(student)

def get_students():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()