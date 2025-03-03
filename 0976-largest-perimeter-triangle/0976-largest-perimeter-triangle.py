class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maxPerimeter=0
        for l in range(len(nums)-2):
            m=l+1
            r=l+2
            if nums[m]+nums[r]>nums[l]:
                maxPerimeter=max(maxPerimeter,nums[m]+nums[r]+nums[l])

        return maxPerimeter
            

        