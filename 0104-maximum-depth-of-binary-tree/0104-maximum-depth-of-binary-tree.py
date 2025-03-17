# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0
            ansLt =depth(root.left)
            ansRt =depth(root.right)
            maxdepth=max(ansLt,ansRt)
            return 1+ maxdepth
        
        return depth(root)