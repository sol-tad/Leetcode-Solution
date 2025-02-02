class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(" ")
        lonStr=max(s,key=len)
        verstr=[]
        for i in range(len(lonStr)):
            curver=""
            for j in range(len(s)):
                if len(s[j])<i+1:
                    curver+=" "
                else:
                    curver+=s[j][i]
            verstr.append(curver.rstrip())
        return verstr

                

        