class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        hmap={}
        snum=sorted(nums)
        for i in range(len(nums)):
            if snum[i] not in hmap:
                hmap[snum[i]]=i
        for i in range(len(nums)):
            res.append(hmap[nums[i]])
        return res