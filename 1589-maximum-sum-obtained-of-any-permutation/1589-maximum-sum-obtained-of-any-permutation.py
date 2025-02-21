class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        linesweep=[0]*(len(nums)+1)
        maxlen=0
        for req in requests:
            l,r=req
            maxlen=max(maxlen,r)
            linesweep[l]+=1
            linesweep[r+1]-=1
        for i in range(1,len(linesweep)):
            linesweep[i]+=linesweep[i-1]
        linesweep.sort(reverse=True)
        nums.sort(reverse=True)
        print(linesweep)
        print(nums)
        print(maxlen)
        total=0
        for i in range(maxlen+1):
            total+=linesweep[i]*nums[i]
        return total%(10**9 + 7)


