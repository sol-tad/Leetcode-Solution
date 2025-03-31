class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high=1,len(nums)-1

        while low<=high:
            mid=(low+high)//2
            count=sum(num<=mid for num in nums) 

            if count > mid:
                high=mid-1  
            else:
                low=mid+1  
        return low  