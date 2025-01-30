class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # If any digit in base-3 is '2', return False
                return False
            n //= 3  # Move to the next base-3 digit
        return True
