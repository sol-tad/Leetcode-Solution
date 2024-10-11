class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nset=set(nums)
        res=[]
        for num in nset:
            if nums.count(num)==2:
                res.append(num)
        return res
