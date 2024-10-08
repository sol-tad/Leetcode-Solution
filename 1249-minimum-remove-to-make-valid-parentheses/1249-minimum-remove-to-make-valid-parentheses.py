class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        open_count=0
        for i in range(len(s)):
            if s[i]=='(':
                open_count+=1
            elif s[i]==')':
                if open_count>0:
                    open_count-=1
                else:
                    s[i]=''
        close_count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                close_count+=1
            elif s[i]=='(':
                if close_count>0:
                    close_count-=1
                else:
                    s[i]=''
        return ''.join(s)


        