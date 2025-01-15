# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def details(self):
        print(self.title, self.author, self.year)
        return


class Novel(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author, year)
        return

    def details(self):
        print(self.title, self.author, self.year)
        return

book1 = Book('Breakthrough', 'habiba', 2020)
print(book1.details())
novel1 = Novel('The Pearl', 'Assumpta', 2020)
print(novel1.details())


# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animals:
    def __init__(self, name):
        self.name = name
        return

    def speak(self):
        print("animal sound")
        return

class Dog(Animals):
    def speak(self):
        print("Barks")

class Cat(Animals):
    def speak(self):
        print("purrs")


animals1 = Animals('animal')
animals1.speak()
dog1 = Dog('dog')
dog1.speak()
cat1 = Cat('cat')
cat1.speak()