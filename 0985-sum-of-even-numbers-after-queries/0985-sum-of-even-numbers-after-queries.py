class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        evensum = sum(num for num in nums if num % 2 == 0)

        for val, index in queries:
            if nums[index] % 2 == 0:
                evensum -= nums[index]

            nums[index] += val

            if nums[index] % 2 == 0:
                evensum += nums[index]

            res.append(evensum)

        return res
        