#create Warrior, Mage, Magic Swordman 
import random

def warrior_stats():
    health = 1000
    attack = 400
    defense = 500
    magic = 100
    value = [health,attack,defense,magic]
    return value

class Warrior:
    
    def __init__(self, name):
        self.name = name
        x = warrior_stats()
        self.health=x[0]
        self.attack=x[1]
        self.defense=x[2]
        self.magic=x[3]
        
    def offense(self,enemy):
        value = random.randrange(((self.attack - 100)/10), ((self.defense)/10))
        
    
        
class Mage:
    health = 1000
    attack = 300
    defense = 200
    magic = 500
    def __init__(self, name):
        self.name = name
        
class Magic_Swordsman(Warrior, Mage):
    health = 1000
    attack = 350
    defense = 500
    magic = 100
    def __init__(self, name):
        self.name = name

w1 = Warrior("Humanity")
m1 = Mage("Eren")

w1.offense(m1   )

