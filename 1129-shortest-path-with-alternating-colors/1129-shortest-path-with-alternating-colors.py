class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    
            red_adj=defaultdict(list)
            blue_adj=defaultdict(list)
            
            for u,v in redEdges:
                red_adj[u].append(v)
            for u,v in blueEdges:
                blue_adj[u].append(v)

            queue=deque()
            queue.append((0, 0, None)) 
            
            visited = set()
            res = [-1] * n

            while queue:
                node,length,last_color = queue.popleft()
                if res[node]==-1:
                    res[node]=length

                if last_color != 'red':
                    for nei in red_adj[node]:
                        if (nei, 'red') not in visited:
                            visited.add((nei, 'red'))
                            queue.append((nei, length + 1, 'red'))

                if last_color != 'blue':
                    for nei in blue_adj[node]:
                        if (nei, 'blue') not in visited:
                            visited.add((nei, 'blue'))
                            queue.append((nei, length + 1, 'blue'))

            return res