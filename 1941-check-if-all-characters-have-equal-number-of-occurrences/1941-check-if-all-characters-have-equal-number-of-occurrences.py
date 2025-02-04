class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hm={}
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]]+=1
            else:
                hm[s[i]]=1
        hmset=set(hm.values())
        if len(hmset)>1:
            return False
        else:
            return True


        