# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total=sum(nums)
#         memo=defaultdict(int)
#         if total % 2 != 0:
#             return 0
        
#         target=total//2

#         def dfs(index,currSum):

#             if currSum==target:
#                 return True
#             if currSum>target or index>=len(nums):
#                 return False
            
#             if ((index,currSum)in memo):
#                 return memo[index,currSum]

#             take=dfs(index+1,currSum+nums[index])
#             leave=dfs(index+1,currSum)

#             if ((index,currSum) not in memo):
#                 memo[index,currSum]= take or leave

#             return take or leave

#         return dfs(0,0)

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        memo = defaultdict(int)

        def dfs(index, currSum):
            if currSum == target:
                return 1
            if currSum > target or index >= len(nums):
                return 0

            if (index, currSum) in memo:
                return memo[(index, currSum)]

            take = dfs(index + 1, currSum + nums[index])
            leave = dfs(index + 1, currSum)

            memo[(index, currSum)] = take or leave
            return memo[(index, currSum)]

        return bool(dfs(0, 0))
