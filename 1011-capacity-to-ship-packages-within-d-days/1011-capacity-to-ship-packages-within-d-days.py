class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity(c):
            day=1
            i=0
            currsum=0
            while i<len(weights):
                currsum+=weights[i]
                if currsum>c:
                    currsum=weights[i]
                    day+=1
                i+=1
                
            return day<=days
      
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            if capacity(mid):
                right=mid-1
            else:
                left=mid+1
        return left