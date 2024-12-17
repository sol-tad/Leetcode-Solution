class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]]+=1
            else:
                hm[nums[i]]=1
        for val in list(hm.values()):
            if val>1:
                return True
        return False

        