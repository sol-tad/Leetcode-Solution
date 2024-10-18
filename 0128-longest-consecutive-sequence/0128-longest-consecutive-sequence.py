class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        numset=list(numsset)
        numset.sort()
        maxcount=0
        currCount=0
        for i in range(1,len(numset)):

            if numset[i-1]+1==numset[i]:
                currCount+=1
            else:
                currCount=0
            maxcount=max(maxcount,currCount)
        return maxcount+1 if len(nums)>0 else 0

        
        