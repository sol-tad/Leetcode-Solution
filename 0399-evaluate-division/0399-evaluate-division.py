class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(src, dest, visited):
            if src not in graph or dest not in graph:
                return -1.0
            if src == dest:
                return 1.0
            visited.add(src)
            for neighbor, val in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dest, visited)
                    if result != -1.0:
                        return result * val
            return -1.0

        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        return results