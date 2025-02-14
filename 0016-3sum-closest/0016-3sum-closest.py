class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        res=float("inf")
        while l<(len(nums)-2):
            m=l+1
            r=len(nums)-1 
            while m<r:
                currsum=nums[l]+nums[m]+nums[r]
                if abs(target-currsum)<abs(target-res):
                    res=currsum 
                if (currsum)<target:
                    m+=1
                else:
                    r-=1
            l+=1

        return res


        
        



        