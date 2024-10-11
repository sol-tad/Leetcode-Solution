class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        
        for num in nums:
            index = abs(num) - 1  # Get the index corresponding to the value
            if nums[index] < 0:
                res.append(abs(num))  # If already negative, it's a duplicate
            else:
                nums[index] = -nums[index]  # Mark it as visited by negating it
                
        return res
