class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        res=[]

        for i in range(len(paths)):
            currlist=paths[i].split()
            for j in range(1,len(currlist)):
                si=currlist[j].index("(")
                ei=currlist[j].index(")")
                content=currlist[j][si+1:ei]
                hm[content].append(currlist[0]+"/"+currlist[j][:si])
       
        for item in list (hm.values()):
            if len(item)>1:
                res.append(item)
        return res

