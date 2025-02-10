class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in range(len(nums)-1,0,-1):
            for i in range(n):
                if  nums[i]> nums[i+1]:
                     nums[i], nums[i+1]= nums[i+1], nums[i]
                    
        