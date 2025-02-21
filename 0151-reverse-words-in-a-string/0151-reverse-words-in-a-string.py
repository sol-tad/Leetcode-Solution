class Solution:
    def reverseWords(self, s: str) -> str:
        strlist=s.split()
        return " ".join(strlist[::-1])
        