class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        sm = 0
        n = len(bank)
        m = len(bank[0])
        res = 0
        for i in range(n):
            sm2 = 0 
            for j in range(m):
                sm2 += bank[i][j] == "1"
                if bank[i][j] == "1":
                    res += sm
            if sm2:
                sm = sm2

        return res
