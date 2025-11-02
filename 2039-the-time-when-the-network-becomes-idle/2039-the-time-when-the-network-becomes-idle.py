class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        dist = [float('inf')] * n
        dist[0] = 0
        q = deque([0])

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if dist[nei] == float('inf'):
                    dist[nei] = dist[node] + 1
                    q.append(nei)
        
        max_time = 0
        for i in range(1, n):
            d = dist[i] * 2  
            if d <= patience[i]:
                last_sent = 0
            else:
                last_sent = ((d - 1) // patience[i]) * patience[i]
            max_time = max(max_time, last_sent + d)
        
        return max_time + 1
