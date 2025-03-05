class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        minmov=0
        while target!=1:
            if maxDoubles>0:
                if target%2==0:
                    target//=2
                    maxDoubles-=1
                    minmov+=1
                elif target%2==1:
                    target-=1
                    minmov+=1
            else:
                minmov+=target-1
                break
        return minmov
                
            



