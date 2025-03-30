import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findRow(mid):
            if matrix[mid][0]>target:
                return 1
            elif matrix[mid][0]<target and matrix[mid][-1]<target:
                return -1
            elif matrix[mid][0]<=target and matrix[mid][-1]>=target:
                return 0
        def bnrsrch(res):
            l=0
            r=len(matrix[res])-1
            while l<=r:
                m=(l+r)//2
                if matrix[res][m]==target:
                    return True
                if matrix[res][m]>target:
                    r=m-1
                else:
                    l=m+1
            return False

        l,r=0,len(matrix)-1
        res=-1
        while l<=r:
            midrow=(l+r)//2
            if findRow(midrow)==-1:
                l=midrow+1
            elif findRow(midrow)==1:
                r=midrow-1
            elif findRow(midrow)==0:
                res=midrow
                break
        return  bnrsrch(res)

             

        