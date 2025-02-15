class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        fptr=0
        sptr=0
        while (fptr<len(firstList) and sptr<len(secondList)):
            if  firstList[fptr][1]<secondList[sptr][0]:
                fptr+=1
            elif  firstList[fptr][0]>secondList[sptr][1]:
                sptr+=1
            else:
                res.append([max(firstList[fptr][0],secondList[sptr][0]),min(firstList[fptr][1],secondList[sptr][1])])
                if firstList[fptr][1]<secondList[sptr][1]:
                    fptr+=1
                else:
                    sptr+=1
        return res






        