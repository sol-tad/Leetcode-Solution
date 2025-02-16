class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        minlen=float("inf")
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                currsum-=nums[l]
                minlen=min(minlen,r-l+1)
                l+=1
        return minlen if minlen!=float("inf") else 0
        