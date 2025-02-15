class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmp=dict(Counter(p))
        size=len(p)
        windowSize=0
        hm=defaultdict(int)
        l=0
        res=[]
        for r in range(len(s)):
            hm[s[r]]+=1
            windowSize+=1
            while windowSize>=size and len(hm)>=len(hmp) :
                if hm==hmp:
                    res.append(l)
                hm[s[l]]-=1
                if hm[s[l]]==0:
                    del hm[s[l]]
                l+=1
                windowSize-=1
        return res


        