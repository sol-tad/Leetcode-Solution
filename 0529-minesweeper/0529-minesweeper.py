class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)]

        def count_mines(r, c):
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count

        def dfs(r, c):
            if board[r][c] != 'E':
                return
            mine_count = count_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        dfs(nr, nc)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            dfs(row, col)

        return board