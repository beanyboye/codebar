"""
By:         Callum Clegg
Date:       22/02/2023

Desc:       Solutions for functions lab.
"""

# 1.    Create a function that returns whether a number even
def is_even(n: int) -> bool:
    pass

# 1a.   Create a function that will loop through a range of n and print all number which are even.
#       Use the previous function.
def even_from_range(min: int, max: int) -> None:
    pass


# 1b.   Can you do this using for in loop? Google this...
def even_from_range(min: int, max: int) -> None:
    pass

# 1c.   Assign a defualt argument to your function
def even_from_range(min: int = 2, max: int = 10) -> None:
    pass

# 2.    Create a function that uses keyword = value syntax to access the following dict
students: dict[str, float] = {
    "Lucy" : 76,
    "David" : 83,
    "Connor" : 62,
    "Amber" : 91
}

def student_grade(student: str) -> float:
    pass


# 3.    Create a funciton that can take any number of arguments of any type, and prints each one.
def print_arguments(*arg: any) -> None:
    pass


# 3a.   Create a function that can take any number of keyword = value arugments to access the students dict
def average_grade(**pupils) -> float:
    pass


# 4.    Create a recursive function that finds the factorial of a number x
def factorial(x: int) -> int:
    pass


if __name__ == "__main__":
    # TEST HARNESS
    pass