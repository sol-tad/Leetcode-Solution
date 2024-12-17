class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            hm={}
            for i in range(len(s)):
                if s[i] in hm:
                    hm[s[i]]+=1
                else:
                    hm[s[i]]=1
            for i in range(len(t)):
                if t[i] in hm:
                    hm[t[i]]-=1
            for val in hm.values():
                if val >0:
                    return False
            return True
        else:
            return False

   
       