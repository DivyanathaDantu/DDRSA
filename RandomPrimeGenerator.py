import random as rand


class RandomPrimeGenerator:
    @staticmethod
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):  # only odd numbers
            if n % i == 0:
                return False
        return True

    def gcd(self, number1, number2):
        if number1 == 0:
            return number2
        else:
            return self.gcd(number2 % number1, number1)

    def generate_random_prime(self):
        num = rand.randrange(2 ** (16 - 1) + 1, 2 ** 16 - 1)
        while not self.is_prime(num):
            num = rand.randrange(2 ** (16 - 1) + 1, 2 ** 16 - 1)
        return num

    def generate_p_q(self):
        p = self.generate_random_prime()
        q = self.generate_random_prime()
        print("16-bit Random prime numbers p,q are", p, "and", q)
        return p, q

    def generate_e(self, p, q):
        phi_of_n = (p - 1) * (q - 1)
        num = rand.randrange(2 ** (16 - 1) + 1, phi_of_n)
        while self.gcd(phi_of_n, num) != 1:
            num = rand.randrange(2 ** (16 - 1) + 1, 2 ** 16 - 1)
        print("random e for given p -", p, ",q-", q, "is", num)
        return num


# rpg = RandomPrimeGenerator()
# prime_1, prime_2 = rpg.generate_p_q()
# rpg.generate_e(prime_1, prime_2)
