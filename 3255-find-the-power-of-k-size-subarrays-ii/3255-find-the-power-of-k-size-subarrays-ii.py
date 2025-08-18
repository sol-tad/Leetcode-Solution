class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        result=[-1]*(n-k+1)
        length = 1
        
        if k ==1:
          return nums

        for i in range(1, n):
            if nums[i] == nums[i-1]+1:
                length += 1
            else:
                length = 1
            if length >= k:
                result[i-k+1] = nums[i]
        
        return result