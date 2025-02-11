class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        hm=defaultdict(int)
        res=[]
     
        for row in range(len(score)):
            hm[row]=score[row][k]
         
        sortedhm = dict(sorted(hm.items(), key=lambda item: item[1],reverse=True))
        
        for k in sortedhm:
            res.append(score[k])
        return res

        