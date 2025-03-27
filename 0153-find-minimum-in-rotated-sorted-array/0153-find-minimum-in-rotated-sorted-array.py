class Solution:
    def findMin(self, nums: List[int]) -> int:
        def valid(r,mid):
            return nums[r] > nums[mid]
        
        l = 0
        r = len(nums)-1
        ans = float('inf')
        while l <= r:
            mid = (l+r)//2    
                 
            if valid(r,mid): 
                r = mid         
                
            else:
                l = mid + 1
        
        return nums[r]