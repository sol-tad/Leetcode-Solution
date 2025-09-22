class Solution:
    def rob(self, nums: List[int]) -> int:
       memo=defaultdict(int)
       def dp(i):
        if i>=len(nums):
            return 0
        if i in memo:
            return memo[i]
        rob=nums[i]+dp(i+2)
        skip=dp(i+1)
        memo[i]=max(rob,skip)
        return memo[i]

       return dp(0)