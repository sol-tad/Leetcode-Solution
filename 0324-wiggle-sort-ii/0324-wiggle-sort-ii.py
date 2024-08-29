class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        
        left = nums[:mid]
        right = nums[mid:]
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = left.pop()
            else:
                nums[i] = right.pop()
