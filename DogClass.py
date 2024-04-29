class Dog:
    def __init__(self,name):
        self.legs=4
        self.name=name
    def speek(self):
        print(self.name+"barks")

myDog = Dog('Rover')
myDog.speek()
type(Dog('Rover'))
