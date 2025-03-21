# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total=0
        def sumtree(root,num):
            nonlocal total
            if not root:
                return
            num+=str(root.val)
            if not root.left and not root.right:
                total+=int(num)
                return
            sumtree(root.left,num)
            sumtree(root.right,num)  
        sumtree(root,"")
        return total

