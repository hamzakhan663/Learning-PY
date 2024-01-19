#Defining multiple classes relating to one another
class Sensei():
    def __init__(self, name):
        self.name=name
        
class EagleFang(Sensei):
    def __init__(self, name, sensei1):
        super().__init__(name)
        self.sensei=sensei1
        
class MiyagiDo(Sensei):
    def __init__(self, name, sensei2):
        super().__init__(name)
        self.sensei2=sensei2
        
ef = EagleFang("Johnny", "Kreese")
md = MiyagiDo("LaRusso", "Terry Silver")
s = Sensei("Chozen")