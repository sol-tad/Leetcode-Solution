class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach 1
        maxStep=0
        for i in range(len(nums)):
            if i>maxStep:
                return False

            maxStep=max(maxStep,i+nums[i])

            if maxStep>=len(nums)-1:
                return True
        return False
        