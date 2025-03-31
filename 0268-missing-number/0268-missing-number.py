class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return ((len(nums)*(len(nums)+1))//2)-sum(nums)
        nums.sort()
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>mid:
                r=nums[mid]-1
            else:
                l=mid+1
        return l