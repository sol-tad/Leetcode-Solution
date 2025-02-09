class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i]  = matrix[j][i], matrix[i][j]
        
        # refection on middle row
        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n-c-1]  = matrix[r][n-c-1], matrix[r][c]

            

        