class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numset=set(nums)
        numarr=[]

        for num in numset:
            if nums.count(num)>len(nums)/3:
                 numarr.append(num)
        return numarr
        