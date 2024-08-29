class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        # compute prfixsum of sorted nums
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        answer=[]
        for i in range(len(queries)):
            j=0
            while j<len(nums) and queries[i]>=nums[j] :
                j+=1
            answer.append(j)
        return answer
        