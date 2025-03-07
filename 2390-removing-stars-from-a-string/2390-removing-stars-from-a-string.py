class Solution:
    def removeStars(self, s: str) -> str:
        s=list(s)
        stack=[]
        for ch in s:
            if ch=="*":
                if stack:
                  stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)