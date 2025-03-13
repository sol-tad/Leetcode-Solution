class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currRowlist=[1]*(rowIndex+1)
        if rowIndex==0:
            return [1]
        res=self.getRow(rowIndex-1)
        for i in range(1,len(currRowlist)-1):
            currRowlist[i]=res[i]+res[i-1]
        return currRowlist