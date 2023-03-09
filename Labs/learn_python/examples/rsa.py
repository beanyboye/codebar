"""
Lab:        Asymmetric Cryptography Implementation (RSA)
Date:       08/03/23

Think:      In this example consider the importance of keeping certain information private
            from the client, take note of the syntax and application of static methods and
            private variables/functions.
"""

import random

class RSA:    
    # This is a formated doc comment
    """ 
        Parameters
        ----------
        arg : int
            number to check is prime
        
        Returns
        -------
        bool
            True for it is prime, False otherwise
    """

    # Use underscores to make larger numbers more readable
    RANGE: int = 1_000

    def __init__(self, p: int, q: int, text: str = "hello world!") -> None:
        # Below are assertions that check that the parameters p and q are infact valid
        assert p != q, "Values p and q cannot be equal!" 

        assert self.__is_prime(p), "p is not a prime number!"
        assert self.__is_prime(q), "q is not a prime number!"
        
        self._n: int = p * q
        self._phi_n: int = (p-1) * (q-1)

        self.pub = self.__generate_pub()
        # We can denote private variables and functions with double underscore...
        # We can denote protected variables and funcitons with one underscore
        self.__pri = self._n, self.__generate_pri()

        self.__text = text
        self.cipher = self.encrypt()

    @staticmethod
    def __is_prime(n: int) -> bool:
        """ Checks if value is in fact prime. """
        if n <= 2 or n % 2 == 0:
            return False

        for check in range(3, n, (n+1)*(n+1)):
             if n % check == 0:
                return False

        return True

    def __generate_pub(self) -> list[int]:
        """ This method generates the value 'e' for the public key (encrypt). """
        potential = list(range(2, self._phi_n))
        results = list();
                
        factors = [i for i in potential if self._phi_n % i == 0 or self._n % i == 0]
        for i in potential:
            for factor in factors:
                if i % factor == 0:
                    break
            else:
                results.append(i)

        return self._n, random.choice(results)

    def __generate_pri(self) -> int:
        """ This method generates the value 'd' for the private key (decrypt). """
        e: int = self.pub[1]
        explore = range(1, self._phi_n * self.RANGE)
        potential = list();
        potential = [i for i in explore if ((e*i) % self._phi_n == 1)]

        return random.choice(potential)

    def encrypt(self) -> str:
        """ This method encrypts plain text on a character by character basis. """
        assert self.pub != None, "public key does not exist!"
        self.cipher = ""

        for char in self.__text:
            self.cipher += chr((ord(char)^self.pub[1]) % self.pub[0])

        return self.cipher

    def decrypt(self) -> str:
        """ This method decrypts data from cipher text on a character by character basis. """

        assert self.__pri != None, "private key does not exist!"

        for char in self.cipher:
            self.__text.replace(char, chr((ord(char)^self.__pri[1]) % self.__pri[0]))
        self.cipher = ""

        return self.__text

if __name__ == "__main__":
    # Test harness
    testing: RSA = RSA(7, 11, "testing")

    print("public:", testing.pub)

    print("encrypted text:", testing.encrypt())
    print("decrypted text:", testing.decrypt())
