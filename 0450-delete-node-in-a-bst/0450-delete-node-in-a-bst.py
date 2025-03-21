# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minNode(root):
            while root.left: 
                root=root.left
            return root
        def delete(root,key):
            if not root:
                return None
            if root.val>key:
                root.left=delete(root.left,key)
            elif root.val<key:
                root.right=delete(root.right,key)
            elif root.val==key:
                if not root.left and not root.right:
                    return None
                
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                
                minRoot=minNode(root.right)
                root.val=minRoot.val
                root.right=delete(root.right,minRoot.val)
            return root
        return delete(root,key)  


