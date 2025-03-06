class Solution:
    def isValid(self, s: str) -> bool:
        hm={")":"(","}":"{","]":"["}
        stack=[]

        for st in s:
            if st in hm:
                if stack and stack[-1]==hm[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        if not stack:
            return True
        else:
            return False
        