class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b_squared=c-a*a
            if b_squared<0:
                continue
            b=int(math.sqrt(b_squared))
            if b*b==b_squared:
                return True
        return False
        