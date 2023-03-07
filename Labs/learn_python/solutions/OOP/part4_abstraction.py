"""
By:         Callum Clegg
Date:       03/06/2023

Desc:       Solution demonstrating the application of abstraction for child classes.
"""

from abc import ABC, abstractmethod # Abstract Base Class (ABC)

# 1.    Create a abstract class called animal using the abc library. 
#       This object should store species, life exptectancy speak attributes.
# 1a.   Create two abstract methods called info() and speak()

class Animal(ABC):

    def __init__(self, species: str, life_expectancy: float, speak: str) -> None:
        """ This a constructor for a abstract base class """
        self._species = species
        self._life_expectancy = life_expectancy
        self._speak = speak

    @abstractmethod
    def info(self) -> None:
        """ This function offers information on a specific animal. """
        pass

    @abstractmethod
    def speak(self) -> None:
        pass

# 2.    Create a class alled Cat that inherits abstract class animal. 
#       Takes all arguments of animal in addition to a new attribute called breed.

# 2a.   Override the methods info and speak from the Animal class printing all attributes in info and
#       pinting the sound of the cat in speak()
class Cat(Animal):

    def __init__(self, species: str, life_expectancy: float, speak: str, breed: str):
        super().__init__(species, life_expectancy, speak)
        self._breed = breed

    def info(self) -> None:
        """ Information about a cat. """
        print(f"""
            species: {self._species}
            life_expectancy: {self._life_expectancy}
            breed: {self._breed}
        """)

    def speak(self) -> None:
        print(f"{self._speak}")

# 3.    Do the exact same as you did in part 2, but for a dog.
class Dog(Animal):

    def __init__(self, species: str, life_expectancy: float, speak: str, breed: str):
        super().__init__(species, life_expectancy, speak)
        self._breed = breed

    def info(self) -> None:
        print(f"""
            name: {self._name}
            species: {self._species}
            life_expectancy: {self._life_expectancy}
            breed: {self._breed}
        """)

    def speak(self) -> None:
        print(f"{self._speak}")

if __name__ == "__main__":
    
    cat = Cat("Felis catus", 12, "meow", "tabby")
    dog = Dog("Canis lupus familiaris", 15, "bark", "sausage dog")

    cat.speak()
    dog.speak()

    cat.info()
    dog.info()

