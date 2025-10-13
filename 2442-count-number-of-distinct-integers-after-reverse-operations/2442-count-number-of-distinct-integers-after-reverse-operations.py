class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique_nums = set()

        for num in nums:
            unique_nums.add(num)
            
            unique_nums.add(int(str(num)[::-1]))  

        return len(unique_nums)
            