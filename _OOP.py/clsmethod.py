import random
class Grade:
    grades = ["Champion", "Advanced", "Intermediate", "Rookie"]
    
    @classmethod
    def sort(cls, name):
        print(f"{name} - {random.choice(cls.grades)} player.")
        
Grade.sort("Hamza")