class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=""
        for i in range(len(s)):
            index=indices.index(i)
            res+=s[index]
            
        return res