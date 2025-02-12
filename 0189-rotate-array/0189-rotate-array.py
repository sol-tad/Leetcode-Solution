class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
      
        # for i in range(k):
        #     nums.insert(0,nums[-1])
        #     nums.pop()
        