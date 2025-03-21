# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def zigzag(root,level):
            nonlocal res

            if not root:
                return
            if len(res)==level:
                res.append(deque())
            if level%2==0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
            zigzag(root.left,level+1)
            zigzag(root.right,level+1)
        
        zigzag(root,0)
        for i in range(len(res)):
            res[i]=list(res[i])
        return res