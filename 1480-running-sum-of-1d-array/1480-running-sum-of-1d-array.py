class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currsum = 0
        for i in range(len(nums)):
            currsum += nums[i]
            nums[i] = currsum

        return nums
