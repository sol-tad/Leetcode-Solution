class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        bits = list(bin(n)[2:])[::-1]  
        odd = 0
        even = 0

        for i in range(len(bits)):
            if bits[i] == '1':
                if i % 2 == 0:  # Even index from right-to-left
                    even += 1
                else:  # Odd index from right-to-left
                    odd += 1
                    
        return [even, odd]
