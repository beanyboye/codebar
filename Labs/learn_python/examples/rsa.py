"""
Lab:        Asymmetric Cryptography Implementation (RSA)
Date:       08/03/23

Think:      In this example consider the importance of keeping certain information private
            from the client, take note of the syntax and application of static methods and
            private variables/functions.
"""


class RSA:

    def __init__(self, p: int, q: int):
        assert(self.__is_prime(p) and self.__is_prime(q))

        self.n = p * q
        self.__phi_n = (p - 1) * (q - 1)
        self.public_key = (self.n, self.__public_key())
        self.__private_key = (self.n, self.__private_key())

    @staticmethod
    def __is_prime(n: int) -> bool:
        """ This is a static private method that calculates if n is prime. """
        if n <= 1 or n % 2 == 0:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1

        return True


    def __public_key(self) -> int:
        pass

    def __private_key(self) -> int:
        pass

    def encrypt(self):
        pass

    def decrypt(self):
        pass

if __name__ == "__main__":
    
    encrypting: RSA = RSA(3, 7)

    encrypting.__private_key()