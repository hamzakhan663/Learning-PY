class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Provide a name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
       

    def __str__(self):
        return f" Hi, {self.name}. Welcome to your house, {self.house}."
    
    

def main():
    print(get_students())
    
def get_students():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()