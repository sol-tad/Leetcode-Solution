class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows=cols=len(image)
        res=[[0]*cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if image[r][c]==1:
                    res[r][cols-c-1]=0
                elif image[r][c]==0:
                    res[r][cols-c-1]=1


                
        return res
        