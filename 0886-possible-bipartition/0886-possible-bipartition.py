class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        colors=[0]*(n+1)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)
        def dfs(node,color):
            colors[node]=color
            for adjecent in graph[node]:
                if colors[adjecent]==0:
                    if not dfs(adjecent,-color):
                        return False
                elif colors[adjecent]==colors[node]:
                    return False

            return True
        
        for person in range(1,n+1):
            if colors[person]==0:
                if not dfs(person,1):
                    return False
        return True
