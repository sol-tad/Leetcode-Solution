class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        sums = [sum(nums[:k])]
        for i in range(k, n):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        m = len(sums)

        left = [0] * m
        best = 0
        for i in range(m):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        max_total = 0
        ans = []
        for mid in range(k, m - k):
            l = left[mid - k]
            r = right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_total:
                max_total = total
                ans = [l, mid, r]

        return ans
