class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
       ps=[sum(nums[:i]) for i in range(1,len(nums)+1) ]
       return ps