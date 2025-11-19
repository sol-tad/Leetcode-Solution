class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        bobTime = [float('inf')] * n

        def findBobPath(node, parent, t):
            if node == 0:
                bobTime[node] = t
                return True

            for nei in graph[node]:
                if nei == parent:
                    continue
                if findBobPath(nei, node, t + 1):
                    bobTime[node] = t
                    return True

            return False

        findBobPath(bob, -1, 0)
        ans = -10**18

        def dfs(node, parent, tA, currSum):
            nonlocal ans

            if tA < bobTime[node]:
                currSum += amount[node]
            elif tA == bobTime[node]:
                currSum += amount[node] // 2
 
            isLeaf = True
            for nei in graph[node]:
                if nei != parent:
                    isLeaf = False
                    dfs(nei, node, tA + 1, currSum)

            if isLeaf:
                ans = max(ans, currSum)

        dfs(0, -1, 0, 0)
        return ans
