"""
By:         Callum Clegg
Date:       17/02/2023

Desc:       Solutions for practicing if statements and loops
"""

######################### CONDITIONS #########################
# 1.    Ask a user for a number, print if it is odd, else it is even!

user_input: str = input("Please enter any number: ")
if int(user_input) % 2 != 0:
    print("{0} is odd!".format(user_input))
else:
    print("{0} is even!".format(user_input))

# 1a.   Can you do this in a ternary operator? Google this...

user_input: str = input("Please enter any number: ")
print("{0} is {1}!".format(user_input,  ("even", "odd")[int(user_input) % 2 != 0]))

# 2.    Create a elif statement which check if two inputs are even or odd, 
# 2a.   


############################ LOOPS ###########################

# 1.    Print all elemnents from this list using a for each loop
fruits: list[str] = ["strawberry", "banana", "apple", "orange"]
for fruit in fruits:
    print(fruit)

# 1a.   Print all elements with a shorthand loop
[print(fruit) for fruit in fruits]

# 2.    Create a for loop which prints all odd numbers between 1 and 10.   
#       use the range function to do this.

for n in range(1, 10):
    if n % 2 != 0:
        print("{0} is odd!".format(n))


# 3.    Create a while loop that prints only prime numbers up to 100.
#       look online for a effient way to calculate this.

count: int = 0

while count < 100:
    i: int = 2
    prime: bool = True
    if count > 1:
        while i*i <= count:
            if count % i == 0:
                prime = False
            i += 1
        if prime:
            print("{0} is prime!".format(count))
    count += 1

# 3a.   Create a function that checks if a number is prime or not (returns boolean)

def is_prime(n: int) -> bool:
    """ This function returns True if n is prime. """
    if n <= 1:
        return False

    i: int = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

count: int = 0
while count < 100:
    if is_prime(count):
        print("{0} is prime!".format(count))
    count += 1
    
    
