

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        ancestors = [set() for _ in range(n)]
        queue = deque([i for i in range(n) if indegree[i] == 0])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return [sorted(list(ancestor)) for ancestor in ancestors]
