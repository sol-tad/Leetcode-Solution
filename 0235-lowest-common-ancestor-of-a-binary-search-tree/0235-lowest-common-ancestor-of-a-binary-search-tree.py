# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=root
        def comAncesror(root):
            nonlocal ans
            if not root:
                return 
            
            if root is p or root is p:
                ans=root 
                return
            elif root.val>q.val and root.val>p.val:
                comAncesror(root.left)
            elif root.val<q.val and root.val<p.val:
                comAncesror(root.right)
            else:  
                ans=root 
                return
        
        comAncesror(root)
        return ans