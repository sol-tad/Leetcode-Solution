class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hm=dict(Counter(nums))
        res=[]
        for k in hm:
            if hm[k]==2:
                res.append(k)
        return res