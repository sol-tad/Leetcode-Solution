class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def bk(start,comb):
            if len(comb)==k:
                res.append(comb.copy())
                return   
            for i in range(start,n+1):
                comb.append(i)
                bk(i+1,comb)
                comb.pop()
        bk(1,[])
        return res