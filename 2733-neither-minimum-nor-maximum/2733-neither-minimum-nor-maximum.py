class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        numSet=list(set(nums))
        numSet.sort()
        n=len(numSet)
       
        if n<=2:
            return -1
        else:
            return numSet[1]
        
        