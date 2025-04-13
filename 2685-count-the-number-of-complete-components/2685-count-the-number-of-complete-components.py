class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=[False]*n
        def dfs(node,nodes):
            visited[node]=True
            nodes.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor,nodes)
        count=0
        for i in range(n):
            if not visited[i]:
                nodes=[]
                dfs(i,nodes)
                edgeCount=0
                for node in nodes:
                    edgeCount+=len(graph[node])
                edgeCount//=2
                k=len(nodes)
                if edgeCount==k*(k-1)//2:
                    count+=1
        return count