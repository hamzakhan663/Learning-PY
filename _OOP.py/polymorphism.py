#Call the same method on multiple objects.


class Gryffindor:
    def __init__(self, name):
        self.name = name
        
    # def __str__(self):
    #     return (f"Welcome to Hogwarts, {self.name}")
     
    def spell(self):
        print (f"{self.name} casts Expecto Patronum🪄")  
         
class Hufflepuff:
    def __init__(self, name):
        self.name = name
    
    def spell(self):
        print (f"{self.name} casts Wingardium Leviosa🪄")  
          
class Slytherin:
    def __init__(self, name):
        self.name = name
        
    def spell(self):
        print (f"{self.name} casts Avada Kedavra🪄")  
        

g1 = Gryffindor("Harry")
h1 = Hufflepuff("Cedric")
s1 = Slytherin("Draco")

for x in (g1, h1, s1):
    x.spell()

# print(g1)