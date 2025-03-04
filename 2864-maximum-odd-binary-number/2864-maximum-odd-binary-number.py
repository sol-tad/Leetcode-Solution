class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hm=Counter(s)
        return ('1'*(hm['1']-1))+'0'*hm['0']+'1'