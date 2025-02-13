class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm=defaultdict(int)
        start,end=0,0
        res=[]
        for i in range(len(s)):
            hm[s[i]]=i
        print(hm)

        for i in range(len(s)):
            end=max(end,hm[s[i]])
            if end==i:
                res.append(end-start+1)
                start=i+1
        return res


        