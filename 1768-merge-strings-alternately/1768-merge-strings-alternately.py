class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        minlen=min(len(word1),len(word2))
        for i in range(minlen):
            res+=word1[i]
            res+=word2[i]
        if len(word1)>len(word2):
            res+=word1[minlen:]
        else:
            res+=word2[minlen:]
        return res


        