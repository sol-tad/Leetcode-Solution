class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for i in range(2**n):
            ans=[]
            k=0
            while i>0:
                if i&1:
                    ans.append(nums[n-k-1])
                k+=1
                i>>=1
            res.append(ans)

        return res