class Solution:
    def minimumSteps(self, s: str) -> int:
        a=list(s)
        minswap=0
        l=0
        r=len(s)-1
        while l<r:
            if s[l]=="0":
                l+=1
            if s[r]=="1":
                r-=1
            elif s[r]=="0" and s[l]=="1":
                a[l],a[r]=a[r],a[l]
                minswap+=abs(r-l)
                l+=1
                r-=1        
        return minswap
        