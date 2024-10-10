class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['A','E','I','O','U','a','e','i','o','u']
        s=list(s)
        l,r=0,len(s)-1
        while l<r:
            if s[l] in v and s[r] in v:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] in v and s[r] not in v:
                r-=1
            elif s[l] not in v and s[r] in v:
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(s)



        