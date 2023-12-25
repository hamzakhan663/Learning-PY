class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Provide a name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f" Hi, {self.name}. Welcome to your house, {self.house}."
    
    # def charms(self):
    #     match self.patronus:
    #         case "Witcher":
    #             return "🐺"
    #         case "Mermaid":
    #             return "🧜🏼‍♀️"
    #         case "Unicorn":
    #             return "🦄" 
    #         case "Knight":
    #             return "🛡️"
    #         case _:
    #             return "🪄"

def main():
    student = get_students()
    # print ("Expecto Patronum!")
    print(student)

def get_students():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()