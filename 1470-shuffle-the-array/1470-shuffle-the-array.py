class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        res=[]

        for i in range(n):
            res.append(l1[i])
            
            res.append(l2[i])
        return res