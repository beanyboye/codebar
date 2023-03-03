"""
By:         Callum Clegg
Date:       23/02/2023

Desc:       Solutions for practicing if statements and loops
"""


# 1.    Create a class called 'Calculator'
# 1a.   Create a constructor which takes two int OR float parameters
# 1b.   Create a function that performs addition on x and y
# 1c.   Create a function that finds the difference between x and y
# 1d.   Create doc comments for each of the funcitons you have made

# 2.    Use __getattribute__ to print the variable 'x'
# 2a.   Use __setattr__ to set the variable 'y' to 10. Print y to verify.

# 3.    Create a static function that can multiply any two numbers together


class Calculator:

    def __init__(self, x: int | float, y: int | float) -> object:
        """ This is a doc comment. """
        self._x = x
        self._y = y

    def add(self) -> float:
        """ This function adds x and y together. """
        return self._x + self._y

    def difference(self) -> float:
        """ This function finds the differenc between x and y. """
        return abs(self._x - self._y)

    @staticmethod
    def multiply(n1: int, n2: int):
        return n1 * n2


if __name__ == "__main__":

    cal: Calculator = Calculator(2, 3)

    print(cal.add())
    print("The difference between x and y is {0}".format(cal.difference()))

    print(cal.__getattribute__("_x"))
    cal.__setattr__("_y", 10)
    print(cal._y)

    print(cal.multiply(2, 3))

