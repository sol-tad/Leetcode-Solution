class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def cheker(index):
            if citations[index]>=len(citations)-index:
                return True
            else:
                return False
        low,high=0,len(citations)-1
        ans=0
        while low<=high:
            mid=(low+high)//2
            if cheker(mid):
                ans=max(ans,len(citations)-mid)
                low=mid+1
            else:
                high=mid-1
        return ans
        