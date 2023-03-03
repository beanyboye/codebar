"""
By:         Callum Clegg
Date:       17/02/2023

Desc:       Basic introduction to python for beginners. 
            Introducing to reading code, refactoring and documentation
"""

class Student:

    def __init__(self, name: str, year: int, modules: dict[str, float], current_grade: float) -> object:
        self._name = name
        self._year = year
        self._modules = modules
        self._current_grade = current_grade

    def print_enrollment(self) -> None:
        for x in self._modules:
            print(x)

    def __getattribute__(self, __name: str) -> any:
        pass
    
    

class Cohort:
    pass