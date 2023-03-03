"""
By:         Callum Clegg
Date:       22/02/2023

Desc:       Solutions for practicing if statements and loops
"""

def my_function():
    pass

# 1.    Create a function that returns whether a number even
def is_even(n: int) -> bool:
    return n % 2 == 0


# 1a.   Create a function that will loop through a range of n and print all number which are even.
#       Use the previous function.
def even_from_range(min: int, max: int) -> None:
    for n in range(min, max):
        if is_even(n):
            print("{0} is even!".format(n))


# 1b.   Can you do this using for in loop? Google this...
def even_from_range(min: int, max: int) -> None:
    [print("{0} is even!".format(n)) for n in range(min, max) if is_even(n)]


# 1c.   Assign a defualt argument to your function
def even_from_range(min: int = 2, max: int = 10) -> None:
    [print("{0} is even!".format(n)) for n in range(min, max) if is_even(n)]


# 2.    Create a function that uses keyword = value syntax to access the following dict
students: dict[str, float] = {
    "Lucy" : 76,
    "David" : 83,
    "Connor" : 62,
    "Amber" : 91
}

def student_grade(student: str) -> float:
    return students[student]


# 3.    Create a funciton that can take any number of arguments of any type, and prints each one.
def print_arguments(*arg: any) -> None:
    for element in arg:
        print(element)


# 3a.   Create a function that can take any number of keyword = value arugments to access the students dict
def average_grade(**pupils) -> float:
    total: float = 0
    for name, grade in pupils.items():
        print("{0} has score of {1}".format(name, grade))
        total += grade
    return total / len(pupils)


# 4.    Create a recursive function that finds the factorial of a number x
def factorial(x: int) -> int:
    if x == 1:
        return x
    else:
        return (x * factorial(x - 1))


if __name__ == "__main__":
    print(is_even(2))


    even_from_range(2, 10)


    print_arguments(2, "hello", '£')


    print("{0}'s average grade is {1}%".format("Lucy", student_grade(student = "Lucy")))


    average: float = average_grade(lucy = students["Lucy"], connor = students["Connor"])
    
    print("average grade is {0}%".format(average))

    print("The factorial of {0} is {1}".format(3, factorial(3)))

