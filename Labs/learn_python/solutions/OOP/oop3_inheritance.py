"""
By:         Callum Clegg
Date:       24/02/2023

Desc:       Solution demonstrating the application of inheritence
"""


# 1.    Create a parent class called Life and create a constructor which takes
#       the kingdom of the life form, the name and it's life expectancy

# 1a.   Create a function called info which prints the following:
#       _NAME_ belongs to the _KINGDOM_ kingdom and has a life expectancy of _LIFE_EXPECTANCY_

class Life: 

    def __init__(self, kingdom: str, name: str, life_expectancy: float) -> None:
        self._kingdom = kingdom
        self._name = name
        self._life_expectancy = life_expectancy

    def info(self) -> None:
        print(f"{self._name} belongs to the {self._kingdom} kingdom and has a life expectancy of {self._life_expectancy}")


# 2.    Create a subclass of Life called Cat and create a constructor with the same arguments as Life, add speak as the final argument.
# 2a.   call super() constructor to initialise animal type in the cat constructor (thus inheriting all of Lifes properties, functions)

# 2b.   Create a function called greet which prints speak.

class Cat(Life):
    
    def __init__(self, kingdom: str, name: str, life_expectancy: float, speak: str) -> None:
        super().__init__(kingdom, name, life_expectancy)
        self._speak = speak
        self.info()

    def greet(self):
        print(self._speak)

# 3.    Initialise a new cat variable, print it's name and call greet()

if __name__ == "__main__":
    cat: Life = Cat("Animal", "cat", 12, "meow")
    print(cat._name)
    print(cat.greet())
