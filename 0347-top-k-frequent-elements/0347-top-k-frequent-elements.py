class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer=[]
        unique_nums = list(set(nums))
        unique_nums.sort()
        res=[]
        
        for i in range(len(unique_nums)):
            answer.append(nums.count(unique_nums[i]))
        for i in range(k):
            j=answer.index(max(answer))
            res.append(unique_nums[j])
            answer[j]=float('-inf')
        return res




        