#Activity 1

# Base class
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        print(f"{self.name} makes a sound.")

    def show_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

# Derived class (Inheritance + Polymorphism)
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks: Woof!")

# Derived class with encapsulation (private variable)
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, "Cat", age)
        self.__color = color  # private attribute

    def speak(self):
        print(f"{self.name} meows: Meow!")

    def get_color(self):
        print(f"{self.name} is a {self.__color} cat.")

# Creating objects
animal1 = Dog("Buddy", 3, "Golden Retriever")
animal2 = Cat("Whiskers", 2, "black")

# Using methods
animal1.show_info()
animal1.speak()
print()
animal2.show_info()
animal2.speak()
animal2.get_color()


#Activity 2

class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky.")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water.")

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for a in animals:
    a.move()


