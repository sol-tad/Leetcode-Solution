class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for dir in logs:
            if dir =="./":
                continue
            elif dir=="../":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return len(stack)