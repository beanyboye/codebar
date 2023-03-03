"""
By:         Callum Clegg
Date:       24/02/2023

Desc:       Solution demonstrating the application of inheritence
"""

from abc import ABC, abstractmethod # Abstract Base Class (ABC)

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
