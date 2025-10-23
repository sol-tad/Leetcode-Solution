class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        count = 0
        left_bound = -1
        last_minK = -1
        last_maxK = -1
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i  
            if nums[i] == minK:
                last_minK = i  
            if nums[i] == maxK:
                last_maxK = i 
                
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - left_bound)
        
        return count
