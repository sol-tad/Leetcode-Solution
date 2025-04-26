class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        color=[0]*n
        def dfs(node):
            if color[node]!=0:
                return color[node]==2
            color[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            color[node]=2
            return True
        safe_nodes=[]
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        return safe_nodes