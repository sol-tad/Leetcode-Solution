class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        evenPs=[0]*len(nums)
        oddPs=[0]*len(nums)

        for i in range(len(nums)):
            if i==0:
                evenPs[0]=nums[0]
                oddPs[0]=0
            elif i%2==0:
                evenPs[i]= evenPs[i-1]+nums[i]
                oddPs[i]=oddPs[i-1]
            else:
                oddPs[i]= oddPs[i-1]+nums[i]
                evenPs[i]=evenPs[i-1]
        ans=0
        for i in range(len(nums)):
            reven=0
            leven=0
            rodd=0
            lodd=0
            if i==0:
                rodd=evenPs[-1]-evenPs[i]
                reven=oddPs[-1]-oddPs[i]
            else:
                lodd=oddPs[i-1]
                leven=evenPs[i-1]
                rodd=evenPs[-1]-evenPs[i]
                reven=oddPs[-1]-oddPs[i]
            if (lodd+rodd)==(leven+reven):
                ans+=1

        return ans

