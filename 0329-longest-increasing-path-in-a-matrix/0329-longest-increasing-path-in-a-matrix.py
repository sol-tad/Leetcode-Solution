class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
        def in_bound(r, c): return 0 <= r < len(mat) and 0 <= c < len(mat[0])
        indegree = defaultdict(int)
        q, level = deque(), 0

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                for x, y in dirs:
                    nr = row + x
                    nc = col + y            
                    if in_bound(nr, nc) and mat[nr][nc] > mat[row][col]: indegree[(row, col)] += 1
                if indegree[(row, col)] == 0: q.append((row, col))

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for x, y in dirs:
                    nr = row + x
                    nc = col + y

                    if in_bound(nr, nc) and mat[nr][nc] < mat[row][col]:
                        indegree[(nr, nc)] -= 1
                        if indegree[(nr, nc)] == 0:
                            q.append((nr, nc))
            level += 1
        
        return level











