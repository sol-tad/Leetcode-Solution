class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference=[]
        for a,b in costs:
            difference.append([a-b,a,b])
        difference.sort()
        
        minCost=0
        for i in range(len(difference)):
            if i<len(difference)//2:
                minCost+=difference[i][1]
            else:
                minCost+=difference[i][2]
        return minCost
