
class Animal:
    
    def vocalise(self):
        pass
    
    def shed(self):
        pass
    
    
class Mammal(Animal):
    
    def shed(self):
        return "It sheds hair"
    
    
class Reptile(Animal):
    
    def shed(self):
        return "It sheds scales"
    

class Elephant(Mammal):

    def vocalise(self):
        return "Trumpet!"


class Lion(Mammal):
    
    def vocalise(self):
        return "Roar!"


class Crocodile(Reptile):
    
    def vocalise(self):
        return "Hiss!"


class Snake(Reptile):
   
    def vocalise(self):
        return "Hiss!"


class Gorilla(Mammal):

    def vocalise(self):
        return "Umm-umm!"


class Lizard(Reptile):
    
    def vocalise(self):
        raise Exception("No sound")
        
