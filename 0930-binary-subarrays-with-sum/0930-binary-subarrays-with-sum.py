class Solution:
    
    def slwAtmost(self,nums,k):
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
        counGoal=self.slwAtmost(nums,goal)
        counGoal_1=self.slwAtmost(nums,goal-1)
        return counGoal-counGoal_1
    
    
    
    




        