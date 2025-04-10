class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]==1:
                    graph[i+1].append(j+1)
                    # graph[j+1].append(i+1)
        print(graph)
        visited=set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        count=0
        for i in range(1,len(isConnected)+1):
            if i not in visited:
                count+=1
                dfs(i)
        return count+len(isConnected)-len(graph)

            
