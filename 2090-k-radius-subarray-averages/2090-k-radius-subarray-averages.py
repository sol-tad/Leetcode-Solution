class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        avg=[]
        if n>=2*k+1:   
            for i in range(k):
                avg.append(-1)
            currsum=sum(nums[0:2*k+1])
            avg.append(currsum//(2*k+1))
            l=1
            for r in range(2*k+1,n):
                currsum-=nums[l-1]
                currsum+=nums[r]
                avg.append(currsum//(2*k+1))
                l+=1
            for i in range(k):
                avg.append(-1)
            return avg
        else:
            for i in range(n):
                avg.append(-1)
            return avg


        


        