class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nset=set(nums)
        res=[]
        for num in nset:
            if nums.count(num)>1:
                res.append(num)
        return res