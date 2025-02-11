class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
        nums =list(map(str, nums))

        nums.sort(key= lambda a:a*10, reverse = True )
        print(nums)

        if nums[0]=='0':
            return "0"
        return "".join(nums)

