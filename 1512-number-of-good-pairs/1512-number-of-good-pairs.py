class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for num in numset:
            numcount=nums.count(num)
            if numcount==2:
                res+=1
            elif numcount>2:
                res+=sum(range(numcount-1, 0, -1))
        return res

        