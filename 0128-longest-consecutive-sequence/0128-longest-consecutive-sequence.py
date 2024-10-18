class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxcount=0
        currCount=0
        for i in range(1,len(nums)):

            if nums[i-1]+1==nums[i]:
                currCount+=1
            else:
                currCount=0
            maxcount=max(maxcount,currCount)
        return maxcount+1 if len(nums)>0 else 0

        
        