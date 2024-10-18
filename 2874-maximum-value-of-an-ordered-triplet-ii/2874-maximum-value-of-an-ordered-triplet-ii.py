class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left = [0] * n
        right = [0] * n
        ans = 0

        maxi = nums[0]
        for i in range(1, n):
            left[i] = maxi
            maxi = max(maxi, nums[i])

        maxi = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = maxi
            maxi = max(maxi, nums[i])

        for i in range(1, n - 1):
            triplet_value = (left[i] - nums[i]) * right[i]
            ans = max(ans, triplet_value)

        return ans