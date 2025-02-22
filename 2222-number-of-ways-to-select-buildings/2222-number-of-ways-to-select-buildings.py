class Solution:
    def numberOfWays(self, s: str) -> int:
        n=len(s)
        prefix0=[0]*(n+1)
        prefix1=[0]*(n+1)
        for i in range(n):
            prefix0[i+1]=prefix0[i]+(1 if s[i]=='0' else 0)
            prefix1[i+1]=prefix1[i]+(1 if s[i]=='1' else 0)
        result=0
        for i in range(1,n-1):
            if s[i]=='0':
                result+=prefix1[i]*(prefix1[n]-prefix1[i+1])
            else:
                result+=prefix0[i]*(prefix0[n]-prefix0[i+1])
        return result