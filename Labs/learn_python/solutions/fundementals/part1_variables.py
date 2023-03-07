"""
By:         Callum Clegg
Date:       23/02/2023

Desc:       Solutions for practicing if statements and loops
"""


# 1.    Create two variables named x and y and assign both a number,
#       Add these two variables together and print the result.

# 1a.   Use type hints

x: int = 2
y: int = 3

print(x + y)

# 1c.   What happens when you assign a variable z to 1.5 but hint as a int not a float?
#       Will this cause an error?

z: int = 1.5
print(x + y + z)


# 2.    Create a list of unordered numbers, sort them, then print each element in the list.
numbers: list[int] = [3, 7, 2, 5, 3, 10, 11]
numbers.sort()
for n in numbers:
    print(n)

# 3.    Create a dict of type where the key is a name of a student and the value is their grade

students: dict[str, int] = {
    "Jeff": 94,
    "Elenor": 100,
}

# 3a.   Print Elenor's grade from the dict and print 'Elenor has a grade of GRADE%'.

print("Elenor has a grade of {0}%".format(students["Elenor"]))

# 3b.   Change the value of Jeff's grade to 98. print this out as you did with Elenor's

students["Jeff"] = 98
print("Jeff has a grade of {0}%".format(students["Jeff"]))

