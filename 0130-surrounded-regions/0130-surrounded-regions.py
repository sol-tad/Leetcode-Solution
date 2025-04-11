class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        visited=set()
        def dfs(r,c):
            if r<0 or c<0 or r==len(board) or c==len(board[0]) or board[r][c]!="O" or (r,c) in visited:
                return
            board[r][c]="B"
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        rows,cols=len(board),len(board[0])
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][cols-1]=="O":
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="B":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
