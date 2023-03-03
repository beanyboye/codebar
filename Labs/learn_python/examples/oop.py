"""
Lab:        Understanding OOP programming principles
Date:       16/02/23

Think:      Think of the other applications of the simple example below, how could concepts such as inheritence, 
            encapsulation, abstraction and polymorphism apply to real world problems?
"""

from abc import ABC, abstractmethod # Abstract Base Class (ABC)

class Animal(ABC):
    """ Parent/Base/Super class """

    def __init__(self, name: str, kingdom: str, description: str, classification: dict[str, str] = {}) -> object:
        self._name              = name
        self._description       = description
        self._kingdom           = kingdom

        if classification != False:
            self._classification    = classification

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def speak():
        pass 

    

class Cat(Animal): # Inheriting functionality from 'Animal' class.
    """ Child/Sub class """

    def __init__(self, saying: str, name: str, kingdom: str, description: str, classification: dict[str, str] = {}) -> object: 
        # A child's constructor will ALWAYS override a parents.
        # The super() function will allow the child class to inherit all methods and attributes from the parent (super) class.
        super().__init__(name, kingdom, description, classification)
        self._saying = saying

    def speak(self) -> None: # Overriding abstract method from parent class. Why would this be helpful?
        print(self._saying)
    
if __name__ == "__main__":
    # Test Harness
    cat: Cat = Cat("meow", "Felis catus", "Animal", "Felis catus is the 5th most successful predator.")
    cat.speak()
    print(cat._description)
    print(cat.get_name())

