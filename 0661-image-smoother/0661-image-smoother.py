class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res=[[0]*len(img[0]) for _ in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[0])):
                tot,count=0,0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if i<0 or i==len(img) or j<0 or j==len(img[0]):
                            continue
                        tot+=img[i][j]
                        count+=1
                res[r][c]=tot//count
        return  res
               