class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        h=0
        if len(citations)==1:
            return 1
        
        for i in range(len(citations)):
            if n-i>=citations[i]:
              h=n-i
              break
        return h