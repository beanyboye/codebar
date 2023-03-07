"""
By:         Callum Clegg
Date:       03/06/2023

Desc:       Solution demonstrating the application of abstraction for child classes.
"""

from abc import ABC, abstractmethod # Abstract Base Class (ABC)

# 1.    Create a abstract class called animal using the abc library. 
#       This object should store species, life exptectancy speak attributes.
# 1a.   Create two abstract methods called info() and speak()


# 2.    Create a class alled Cat that inherits abstract class animal. 
#       Takes all arguments of animal in addition to a new attribute called breed.
# 2a.   Override the methods info and speak from the Animal class printing all attributes in info and
#       pinting the sound of the cat in speak()


# 3.    Do the exact same as you did in part 2, but for a dog.

if __name__ == "__main__":
    """ Test your solution here... """
    pass