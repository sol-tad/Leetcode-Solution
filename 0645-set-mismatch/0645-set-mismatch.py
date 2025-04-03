class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        hm=Counter(nums)
        print(nums)
        rep=-1
        mis=-1
       
        for k in hm:
            if hm[k]>1:
                rep= k
                break
        curr=1
        i=0
        while i< len(nums):
            if nums[i]==rep:
                i+=1
            if curr!=nums[i]:
                mis=curr
                break
            i+=1
            curr+=1
        if mis==-1:
            mis=len(nums)
            
        return [rep,mis]