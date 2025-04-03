class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        hm=Counter(nums)
        rep=-1
        mis=-1
        i=1
        for k in hm:
            if hm[k]>1:
                rep= k
                break
        for i,num in enumerate(nums):
            if i+1!=num:
                mis=i+1
                break
        return [rep,mis]