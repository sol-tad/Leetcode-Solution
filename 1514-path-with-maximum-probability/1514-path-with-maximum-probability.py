class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:


        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        maxProb = [0.0] * n
        maxProb[start] = 1.0
        heap = [(-1.0, start)]
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob
            if node == end:
                return prob
            if prob < maxProb[node]:
                continue
            for nei, p in graph[node]:
                newProb = prob * p
                if newProb > maxProb[nei]:
                    maxProb[nei] = newProb
                    heapq.heappush(heap, (-newProb, nei))
        
        return 0.0
