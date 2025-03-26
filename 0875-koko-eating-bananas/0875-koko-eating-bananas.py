class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko(bananas):
            res=0
            for n in piles:
                res+=ceil(n/bananas)
            return res<=h
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            if koko(mid):
                high=mid-1
            else:
                low=mid+1
        return low