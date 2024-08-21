class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        currmin=float('inf')
        currmax=float('inf')
        count=0

        for start in range(len(nums)):
            for end in range(start,len(nums)):
                currmin=min(nums[start:end+1])
                currmax=max(nums[start:end+1])
                if currmin==minK and currmax==maxK:
                    count+=1
        return count