class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(queries)):
            nums[queries[i][-1]]+=queries[i][0]
            evensum=0
            for j in range(len(nums)):
                if nums[j]%2==0:
                    evensum+=nums[j]
            res.append(evensum)
        return res

        