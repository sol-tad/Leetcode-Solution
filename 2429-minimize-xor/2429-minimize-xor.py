class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1 = bin(num1).count('1')
        count2 = bin(num2).count('1')
        x = num1
        
        if count1 == count2:
            return num1
        
        elif count1 > count2:
            diff = count1 - count2
            for i in range(32):
                if x & (1 << i):
                    x ^= (1 << i)
                    diff -= 1
                    if diff == 0:
                        break
        else:
            diff = count2 - count1
            for i in range(32):
                if x & (1 << i) == 0:
                    x |= (1 << i)
                    diff -= 1
                    if diff == 0:
                        break
        
        return x
