# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root=TreeNode(nums[m])
            root.left=bst(l,m-1)
            root.right=bst(m+1,r)
            return root
        return bst(0,len(nums)-1)