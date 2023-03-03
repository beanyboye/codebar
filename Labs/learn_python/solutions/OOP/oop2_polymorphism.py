"""
By:         Callum Clegg
Date:       24/02/2023

Desc:       Solution demonstrating the application of polymorphism in a functional and object oriented context.
"""

# 1.    Create a function that can add two numbers together, can it take integers and floats?
# 1a.   add "hello" and "world", what is the output?

def add(x, y):
    return x + y

# 2.    Create two classes of any animal, these classes should contain the age and name of the animal,
# 2a.   Create two methods for each class called info and speak, info should print the age and name of the animal,
#       Speak should print out the noise the animal makes (e.g. a dog 'barks')

# 2b.   Use a for each loop to call info and speak from cat and dog classes, pack these objects into a tuple to do this.
    
class Dog:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def info(self) -> None:
        print(f"I am a dog and my name is {self._name}, I am {self._age} years old.")

    def speak(self) -> None:
        print("bark")

class Cat:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def info(self) -> None:
        print(f"I am a cat and my name is {self._name}, I am {self._age} years old.")

    def speak(self) -> None:
        print("meow")

if __name__ == "__main__":

    # One function can add three types of data...
    print(add(2, 4))                # adding integers
    print(add(2.5, 7.2))            # adding floats
    print(add("hello", "world"))    # adding strings

    cat = Cat("Terry", 5)
    dog = Dog("Josh", 7)

    for animal in (cat, dog):
        animal.speak()
        animal.info()
        animal.speak()



