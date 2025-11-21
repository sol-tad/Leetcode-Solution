class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        dist = [[INF]*26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            dist[u][v] = min(dist[u][v], w)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total = 0
        for s, t in zip(source, target):
            u = ord(s) - 97
            v = ord(t) - 97
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]

        return total
