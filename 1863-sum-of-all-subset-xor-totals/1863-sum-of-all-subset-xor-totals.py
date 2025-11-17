class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0

        def dfs(i, curr):
            if i == len(nums):
                self.ans += curr
                return
            dfs(i + 1, curr ^ nums[i])
            dfs(i + 1, curr)

        dfs(0, 0)
        return self.ans
