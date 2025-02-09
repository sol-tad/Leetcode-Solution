class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for r in range(9):
            rowset=set()
            for c in range(9):
                if board[r][c] in rowset:
                    return False
                elif board[r][c] !=".":
                    rowset.add(board[r][c])
        # check each colomun
        for c in range(9):
            colset=set()
            for r in range(9):
                if board[r][c] in colset:
                    return False
                elif board[r][c]!=".":
                    colset.add(board[r][c])
        # check each 3x3
        start=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for startRow,startCol in start:
            boxset=set()
            for r in range(startRow,startRow+3):
                for c in range(startCol,startCol+3):
                    if board[r][c] in boxset:
                        return False
                    elif board[r][c]!=".":
                        boxset.add(board[r][c])
        return True


                    
            




            

        