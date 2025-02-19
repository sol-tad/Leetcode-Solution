class Solution:
    def maxScore(self, s: str) -> int:
        # res=float("-inf")
        # for i in range(len(s)-1): 
        #     res=max(res,(s[:i+1].count('0')+s[i+1:].count('1')))
        # return res
        ans=float('-inf')
        prfixLeft=[0]*len(s)
        suffixRight=[0]*len(s)
        zero=0
        for i in range(len(s)):
            if s[i]=='0':
                zero+=1
            prfixLeft[i]=zero

        one=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                one+=1
            suffixRight[i]=one
        
        for i in range(len(s)-1):
            ans=max(ans,prfixLeft[i]+suffixRight[i+1])

        return ans