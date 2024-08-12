class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        
        for i in range(len(nums)):
            left_sum=right_sum=0
            if i==0:
                left_sum=0
            else:
                left_sum=nums[i-1]
            right_sum=nums[len(nums)-1]-nums[i]
            if left_sum==right_sum:
                return i
        return -1


        

            
        