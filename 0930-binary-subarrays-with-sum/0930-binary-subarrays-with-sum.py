class Solution:
    
    def slAtmost(self,nums,k):
        l=0
        currsum=0
        count=0
        for r in range(len(nums)):
            currsum+=nums[r]
            while l<=r and currsum>k:
                currsum-=nums[l]
                l+=1
            count+=r-l+1
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counGoal=self.slAtmost(nums,goal)
        counGoal_1=self.slAtmost(nums,goal-1)
        return counGoal-counGoal_1
    
    
    
    




        