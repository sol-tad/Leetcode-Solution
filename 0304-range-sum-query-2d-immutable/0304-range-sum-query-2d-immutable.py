class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r=len(matrix)
        c=len(matrix[0])
        self.psa=[[0 for i in range(c)] for j in range(r) ]
        

        for row in range(r):
            for col in range(c):
                if row==0 and col==0:
                    self.psa[0][0]=matrix[0][0]
                elif row==0 and col>0:
                    self.psa[row][col]=self.psa[row][col-1]+matrix[row][col]
                elif col==0 and row>0:
                     self.psa[row][col]=self.psa[row-1][col]+matrix[row][col]
                else:
                    self.psa[row][col]=self.psa[row-1][col]+self.psa[row][col-1]+matrix[row][col]-self.psa[row-1][col-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1==0 and col1==0:
            return self.psa[row2][col2]
        elif row1==0 and col1>0:
            return self.psa[row2][col2]-self.psa[row2][col1-1]

        elif col1==0 and row1>0:
             return self.psa[row2][col2]-self.psa[row1-1][col2]
        
        else:
            return self.psa[row2][col2]-self.psa[row1-1][col2]-self.psa[row2][col1-1]+self.psa[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)