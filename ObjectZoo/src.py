
class Animal:
    def vocalise(self) -> str:
        raise NotImplementedError("Must be overridden in subclass")
    
    def shed(self) -> str:
        raise NotImplementedError("Must be overridden in subclass")
    
class Elephant(Animal):
    def vocalise(self) -> str:
        return "Trumpet!"
    
    def shed(self) -> str:
        return "It sheds hair"
    
class Lion(Animal):
    def vocalise(self) -> str:
        return "Roar!"
    
    def shed(self) -> str:
        return "It sheds hair"
    
class Crocodile(Animal):
    def vocalise(self) -> str:
        return "Hiss!"
    
    def shed(self) -> str:
        return "It sheds scales"
    
class Snake(Animal):
    def vocalise(self) -> str:
        return "Hiss!"
    
    def shed(self) -> str:
        return "It sheds skin"
