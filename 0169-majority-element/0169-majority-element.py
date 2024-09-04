class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numset=set(nums)

        for num in numset:
            if nums.count(num)>=len(nums)/2:
                return num

        
