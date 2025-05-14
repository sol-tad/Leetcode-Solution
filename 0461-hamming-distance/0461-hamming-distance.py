class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x^y).count('1')
        count=0
        while x > 0 or y>0:
            if (x & 1 == 1 and  y & 1 == 0) or (x & 1 == 0 and  y & 1 == 1) :
                count += 1
            x>>= 1
            y>>= 1
        return count