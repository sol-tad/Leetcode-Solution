class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(largesum):
            subarr=0
            cursum=0
            for n in nums:
                cursum+=n
                if cursum>largesum:
                    subarr+=1
                    cursum=n
            return subarr+1<=k
        l=max(nums)
        r=sum(nums)
        ans=r
        while l<=r:
            mid=l+((r-l)//2)
            if helper(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        