
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0:
                new_index = (i + nums[i]) % n
                res.append(nums[new_index])
            elif nums[i] < 0:
                steps = abs(nums[i])
                new_index = (i - steps + n) % n
                res.append(nums[new_index])
            else:
                res.append(0)
        
        return res