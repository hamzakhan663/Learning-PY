import random

class Grade:
    def __init__(self):
        self.classes = ['Year 11 A - The Admirable', 'Year 11 B - The Brave', 'Year 11 C - The Clever', 'Year 11 D - The Daring', 'Year 11 E - The Efficient', 'Year 11 F - The Fearless', 'Year 11 G - The Glorious', 'Year 11 H - The Harmonious', 'Year 11 I - The Impeccable', 'Year 11 J - The Jolly', 'Year 11 K - The Kindhearted', 'Year 11 L - The Lighthearted', 'Year 11 M - The Magnificent']
        
    def sort(self, name):
        print(f"You, {name} are in {random.choice(self.classes)}.")
        

name = input("What is your name?: ").strip()   
grade = Grade()
grade.sort(name)