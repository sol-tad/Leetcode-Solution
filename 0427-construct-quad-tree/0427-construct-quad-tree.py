"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,startrow,startcol):
            issame=True
            for i in range(n):
                for j in range(n):
                    if grid[startrow][startcol]!=grid[i+startrow][j+startcol]:
                        issame=False
                        break
            if issame:
                return Node(grid[startrow][startcol],True)
            n=n//2
            topleft=dfs(n,startrow,startcol)
            topright=dfs(n,startrow,startcol+n)
            bottomleft=dfs(n,startrow+n,startcol)
            bottomright=dfs(n,startrow+n,startcol+n)
            return Node(0,False,topleft,topright,bottomleft,bottomright)
        return dfs(len(grid),0,0)

