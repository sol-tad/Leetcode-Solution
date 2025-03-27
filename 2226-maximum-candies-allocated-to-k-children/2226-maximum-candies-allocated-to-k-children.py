class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def helper(candy):
            count=0
            for c in candies:
                if c//candy>0:
                    count+=1
            return count>=k
        low,high=1,max(candies)
        res=0
        while low<=high:
            mid=(low+high)//2
            if helper(mid):
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
