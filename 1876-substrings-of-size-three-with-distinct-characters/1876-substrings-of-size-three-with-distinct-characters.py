class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        start=middle=end=good=0
        while start<len(s)-2:
            middle=start+1
            end=middle+1
            if s[start]!=s[middle] and s[start]!=s[end] and s[end]!=s[middle]:
                good+=1
            start+=1
        return good