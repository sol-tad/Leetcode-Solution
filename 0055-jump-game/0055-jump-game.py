class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach 1
        maxIndexReached=0
        for i in range(len(nums)):
            if i>maxIndexReached:
                return False

            maxIndexReached=max(maxIndexReached,i+nums[i])

            if maxIndexReached>=len(nums)-1:
                return True
        
        