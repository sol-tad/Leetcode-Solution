class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        dirs = {
            1: [(0, -1), (0, 1)],      
            2: [(-1, 0), (1, 0)],      
            3: [(0, -1), (1, 0)],      
            4: [(0, 1), (1, 0)],       
            5: [(0, -1), (-1, 0)],     
            6: [(0, 1), (-1, 0)]      
        }
        
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        from collections import deque
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while q:
            x, y = q.popleft()
            if (x, y) == (m - 1, n - 1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if opposite[(dx, dy)] in dirs[grid[nx][ny]]:
                        visited.add((nx, ny))
                        q.append((nx, ny))
        
        return False
