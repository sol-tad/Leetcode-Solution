class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        res=[]
        for i in range(len(words)):
            currset=set(words[i].lower())
            if currset<=r1 or currset<=r2 or currset<=r3 :
                res.append(words[i])
     
        return res
