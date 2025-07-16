class Animal:
    def __init__(self, name, species="Unknown", age=0):
        self.species = species
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    @override
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    @override
    def speak(self):
        print("Meow!")
        
        
def main():
    dog = Dog(name="Buffy", breed="Chihuahua")
    cat = Cat(name="Tom", color="Black")

    print(f"{dog.name} says: ", end="")
    dog.speak()

    print(f"{cat.name} says: ", end="")
    cat.speak()
    
main()