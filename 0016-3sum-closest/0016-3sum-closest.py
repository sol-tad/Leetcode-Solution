class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        res=float("inf")
        nums.sort()

        while (l+1)<r:
            currsum=0
            for m in range(l+1,r):
                currsum=nums[l]+nums[m]+nums[r]
                if abs(currsum-target)<abs(res-target):
                    res=currsum
            if abs(nums[l]-target)> abs(nums[r]-target):
                l+=1
            elif abs(nums[l]-target)< abs(nums[r]-target):
                r-=1
            else:
                l+=1
                r-=1

        return res



        