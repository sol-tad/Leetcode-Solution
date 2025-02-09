class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        cols=len(mat[0])
        res=[]
        currRow=currCol=0
        up=True

        while len(res)!=rows*cols:
            if up:
                while currRow>=0 and currCol<cols:
                    res.append(mat[currRow][currCol])
                    currRow-=1
                    currCol+=1

                if currCol==cols:
                    currCol-=1
                    currRow+=2
                else:
                    currRow+=1
                up=False
            else:
                while currRow<rows and currCol>=0:
                    res.append(mat[currRow][currCol])
                    currRow+=1
                    currCol-=1
                if currRow==rows:
                    currCol+=2
                    currRow-=1
                else:
                    currCol+=1
                up=True
        return res









        