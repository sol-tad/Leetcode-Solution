class Solution:
    def numberOfWays(self, start: int, end: int, k: int) -> int:
        if k < (end-start):
            return 0
        MOD = 10**9 + 7
        if (k - (end-start))%2:
            return 0
      
        return comb(k,((k-(end-start))//2))%MOD