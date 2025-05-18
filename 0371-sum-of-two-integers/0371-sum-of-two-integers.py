class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=(1<<32)-1
        MAX_INT=(1<<31)-1
        while b != 0:
            carry = a & b
            a = (a ^ b)&MASK
            b = (carry << 1)&MASK
        return a if a <= MAX_INT else ~(a^MASK)