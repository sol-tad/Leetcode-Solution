class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm=dict(Counter(nums))
        res=[]
        for k in hm:
            if hm[k]>len(nums)//3:
                res.append(k)
        return res

        