class Solution:
    def binary_exponentitation(self, base, exponent):
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % (10**9 + 7)
            base = (base * base) % (10**9 + 7)
            exponent >>= 1
        return result % (10**9 + 7)

    def countGoodNumbers(self, n: int) -> int:
        even_count, prime_count = 5, 4
        n_prime = n // 2
        n_even = n - n_prime
        num1 = self.binary_exponentitation(even_count, n_even) 
        num2 = self.binary_exponentitation(prime_count, n_prime) 
        return (num1 * num2) % (10**9 + 7)
        