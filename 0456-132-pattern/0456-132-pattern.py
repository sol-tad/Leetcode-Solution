class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')  
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] < third:
                return True  
            while stack and nums[j] > stack[-1]:
                third = stack.pop()  
            stack.append(nums[j])
        return False 