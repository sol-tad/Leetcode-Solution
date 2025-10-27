class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        maxD = deque()  
        minD = deque()  
        left = 0
        res = 0
        for right, num in enumerate(nums):
            while maxD and num > maxD[-1]:
                maxD.pop()
            maxD.append(num)
            
            while minD and num < minD[-1]:
                minD.pop()
            minD.append(num)
            
            while maxD[0] - minD[0] > limit:
                if nums[left] == maxD[0]:
                    maxD.popleft()
                if nums[left] == minD[0]:
                    minD.popleft()
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
