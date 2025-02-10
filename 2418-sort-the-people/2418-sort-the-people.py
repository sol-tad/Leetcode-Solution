class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for n in range(len(heights)-1,0,-1):
            for i in range(n):
                if  heights[i]< heights[i+1]:
                     heights[i], heights[i+1]= heights[i+1], heights[i]
                     names[i], names[i+1]= names[i+1], names[i]
        return names