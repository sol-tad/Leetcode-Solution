class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for c in range(len(matrix[0])):
            curr=[]
            for r in range(len(matrix)):
                curr.append(matrix[r][c])
            res.append(curr)
        return res