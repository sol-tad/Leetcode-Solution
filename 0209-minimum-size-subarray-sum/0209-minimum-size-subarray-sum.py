class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float('inf')
        l,currsum=0,0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                length=min(length,r-l+1)
                currsum-=nums[l]
                l+=1
        return 0 if length==float('inf') else length


        