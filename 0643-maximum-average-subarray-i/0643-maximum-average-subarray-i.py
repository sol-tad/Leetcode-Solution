class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum=sum(nums[:k])
        ava=currsum/k
        start=0
        for i in range(k,len(nums)):
            currsum-=nums[start]
            currsum+=nums[i]
            ava=max(ava,currsum/k)
            start+=1
        return ava


        