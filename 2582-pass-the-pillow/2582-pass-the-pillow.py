class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == 1:
            return 1
        cycle = 2 * (n - 1)
        effective_time = time % cycle
        if effective_time <= n - 1:
            return effective_time + 1
        else:
            return 2 * (n - 1) - effective_time + 1