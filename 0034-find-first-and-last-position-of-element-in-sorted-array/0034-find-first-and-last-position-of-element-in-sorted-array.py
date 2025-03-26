class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        First,Last=-1,-1
        low,high=0,len(nums)-1
        flag=False
        # lower Bound
        while low<=high:
            m=(low+high)//2
            if nums[m]>=target:
                high=m-1
            else:
                low=m+1
        if low<len(nums) and nums[low]==target: 
            First=low

        low,high=0,len(nums)-1
        # upper Bound
        while low<=high:
            m=(low+high)//2
            if nums[m]<=target:
                low=m+1
            else:
                high=m-1
                
        if high>=0 and nums[high]==target:
            Last=high
        return [First,Last]




        

            

