class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # create num -> cost pair and then sort that hepls to get the median nums that      
        # optimize the cost
        numsCostPair=sorted(list(zip(nums,cost)))

        totcost=sum(cost)
        medianNum=None
        runningCostSum=0

        # find the median number
        for num,costt in numsCostPair:
            runningCostSum+=costt
            if runningCostSum>=totcost//2:
                medianNum=num
                break
        
        # after finding the median number then calculate the optimized cost bu performing 
        # increase or decrease by 1 from num towards the medium num
        mincost=0

        for i  in range(len(nums)):
            if nums[i]!=medianNum:
                mincost+=abs(nums[i]-medianNum)*cost[i]
        return mincost

        




        