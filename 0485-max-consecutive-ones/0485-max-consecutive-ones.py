class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        currcount=0
        for n in nums:
            if n!=1:
                currcount=0
            else:
                currcount+=1
            count=max(count,currcount)
        return count