class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            nmat=[[0]*len(mat) for _ in range(len(mat))]

            for r in range(len(mat)):
                for c in range(len(mat)):
                    nmat[r][c]=mat[len(mat)-c-1][r]
            if nmat==target:
                return True
            mat=nmat.copy()
            print("--",mat)
        return False
            
    
    

            