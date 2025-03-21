# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currsum=0
        def gst(root):
            nonlocal currsum
            if not root:
                return root
            gst(root.right)
            # temp=root.val
            currsum+=root.val
            root.val=currsum
            gst(root.left)
        
        gst(root)
        return root
        