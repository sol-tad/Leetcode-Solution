class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currSum=0
        hm=defaultdict(int)
        hm[0]=1

        for num in nums:
            currSum+=num
            if currSum-k in hm:
                res+=hm[currSum-k]
            hm[currSum]+=1
        return res
        