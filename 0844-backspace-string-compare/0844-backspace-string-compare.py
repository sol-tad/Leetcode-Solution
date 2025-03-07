class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS=[]
        stackT=[]
        for c in s:
            if c!="#":
                stackS.append(c)
            else:
                if stackS:
                    stackS.pop()
        s=''.join(stackS)
        for c in t:
            if c!="#":
                stackT.append(c)
            else:
                if stackT:
                    stackT.pop()
        t=''.join(stackT)
        print(stackS)
        print(stackT)
        return s==t

