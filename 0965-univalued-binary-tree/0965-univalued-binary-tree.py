# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val=root.val
        queue=deque([root])
        while queue:
            currnode=queue.popleft()
            if currnode.val!=val:
                return False
            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)
        return True
