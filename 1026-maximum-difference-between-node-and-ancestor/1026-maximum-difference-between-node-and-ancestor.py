# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=float("-inf")
        def dfs(root,maxval,minval):
            nonlocal ans
            if not root:
                return maxval-minval
            maxval=max(maxval,root.val)
            minval=min(minval,root.val)

            leftNodeVal=dfs(root.left,maxval,minval)
            rightNodeVal=dfs(root.right,maxval,minval)
            ans=max(ans,leftNodeVal,rightNodeVal)
            
            return max(leftNodeVal,rightNodeVal)

        dfs(root,float("-inf"),float("inf"))
        return ans