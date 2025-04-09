"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        for emp in employees:
            graph[emp.id]=[emp.importance,emp.subordinates]
        
        # print(graph)
        # print("\n")
        # print(graph[1][1])
        def dfs(node):
            # print(node)
            if len(graph[node][1])==0:
                return graph[node][0]
            ans=0
            for adj in graph[node][1]:
                ans+=dfs(adj)
            return graph[node][0] + ans
        return dfs(id)
