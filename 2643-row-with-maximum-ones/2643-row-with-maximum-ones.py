class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        hm=defaultdict(int)
        maxsum=0
        index=0
       
        for r in range(len(mat)):
            currsum=sum(mat[r])
            if currsum>maxsum:
                index=r
                maxsum=currsum  
        return [index,maxsum]

