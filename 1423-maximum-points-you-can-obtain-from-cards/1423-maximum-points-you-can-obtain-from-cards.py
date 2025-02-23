class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
       tot=sum(cardPoints)
       l=0
       i=len(cardPoints)-k # num of cards that are going to be exclude
       windowsum=sum(cardPoints[:i])
       minSumpoint=windowsum
       for r in range(i,len(cardPoints)):
            windowsum+=cardPoints[r]
            windowsum-=cardPoints[l]

            minSumpoint=min(minSumpoint,windowsum)
            l+=1
            
       return (tot-minSumpoint)



        

        