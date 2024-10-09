class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = (len(b) + len(a)+1)//(min(len(b) ,len(a)))

        for r in range(1,n+1):
            s=a*(r)
            if b in s:
                return r

        return -1
