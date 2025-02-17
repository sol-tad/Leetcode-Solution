class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodprefix=[]
        prodsuffix=[0]*len(nums)

        prod=1
        res=[]
        for n in nums:
            prod*=n
            prodprefix.append(prod)

        prod2=1
        for i in range(len(nums)-1,-1,-1):
            prod2*=nums[i]
            prodsuffix[i]=prod2
        for i in range(len(prodprefix)):
            if i==0:
                res.append(prodsuffix[i+1])
            elif i==(len(prodprefix)-1):
                res.append(prodprefix[i-1])
            else:
                 res.append(prodprefix[i-1]*prodsuffix[i+1])

        return res
