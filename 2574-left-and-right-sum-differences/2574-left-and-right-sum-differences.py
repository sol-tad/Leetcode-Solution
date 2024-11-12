class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ps=[sum(nums[:i]) for i in range(1,len(nums)+1)]
        answer=[]
        for i in range(len(nums)):
            if i==0:
                answer.append(ps[-1]-ps[i])
            elif i==len(nums)-1:
                answer.append(ps[i-1])
            else:
                answer.append(abs(ps[i-1]-(ps[-1]-ps[i])))
            

        return answer

        