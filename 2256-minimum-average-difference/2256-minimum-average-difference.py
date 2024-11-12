from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum = 0
        min_diff = float('inf')
        min_index = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            left_avg = prefix_sum // (i + 1)

            if i < len(nums) - 1:
                right_avg = (total_sum - prefix_sum) // (len(nums) - i - 1)
            else:
                right_avg = 0

            avg_diff = abs(left_avg - right_avg)

            if avg_diff < min_diff:
                min_diff = avg_diff
                min_index = i

        return min_index

