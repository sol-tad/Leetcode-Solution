class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
            left=0
            used=0
            max_len=0
            for right in range(len(nums)):
                while (used & nums[right])!=0:
                    used ^= nums[left] 
                    left += 1
                used|=nums[right]
                max_len=max(max_len,right-left+1)
            return max_len