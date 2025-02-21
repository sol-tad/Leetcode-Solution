class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mxcandy=max(candies)
        res=[]
        for i in range(len(candies)):

            
            res.append((candies[i]+extraCandies)>=mxcandy)
        return res
        