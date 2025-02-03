class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numset=set()
        for i in range(len(ranges)):
            numset.update(ranges[i])
        
        if left not in numset or right not in numset :
                   return False
        elif len(numset)==2:
            return True
        else:
            for i in range(left,right+1):
                if i not in numset :
                     return False
               
        return True
