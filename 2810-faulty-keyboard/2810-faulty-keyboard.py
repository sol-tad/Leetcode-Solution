class Solution:
    def finalString(self, s: str) -> str:
        s=list(s)

        for i in range(len(s)):
            if s[i]=='i':
                s[:i]=reversed(s[:i])
                s[i]=''
        return ''.join(s)