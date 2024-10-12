class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nstr=str(nums[i])
            nlist=list(nstr)
            sum=0
            for num in nlist:
                sum+=int(num)
            nums[i]=sum
        return min(nums)
        