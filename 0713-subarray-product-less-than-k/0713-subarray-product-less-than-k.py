class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        currprod=1
        l=0
        if k==0:
            return 0
        for r in range(len(nums)):
            currprod*=nums[r]
            while currprod>=k and l<=r:
                currprod//=nums[l]
                l+=1  
            count+=r-l+1
        return count


