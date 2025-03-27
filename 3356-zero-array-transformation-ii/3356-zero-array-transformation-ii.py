class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def zerocheck(m):
            linesweep=[0]*(len(nums)+1)
            for i in range(0,m+1):
                l=queries[i][0]
                r=queries[i][1]
                val=queries[i][2]
                linesweep[l]+=val
                linesweep[r+1]-=val
            print(linesweep)
            ps=0
            for i in range(len(nums)):
                ps+=linesweep[i]
                if (nums[i]-ps)>0:
                    return False
            return True
        low,high=0,len(queries)-1
        res=-1
        if max(nums)<=0:
            return 0
        while low<=high:
            mid=(low+high)//2
            if zerocheck(mid):
                res=mid+1
                high=mid-1
            else:
                low=mid+1
        return res

                