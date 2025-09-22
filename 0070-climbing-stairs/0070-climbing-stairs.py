class Solution:
    def climbStairs(self, n: int) -> int:
        mp = defaultdict(int)
        def solu(n):
            if n == 1:
                return 1
            if n == 0:
                return 1
            if n not in mp:
                mp[n] = solu( n - 1) + solu(n - 2)
            return mp[n]
        return solu(n)