# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt  = 0
        num = 0
        def aveg(node):
            nonlocal cnt
            nonlocal num
            if node is None:
                return 0, 0
            left ,il = aveg(node.left)
            right,ir = aveg(node.right) 
            i=il+ir+1

            total = node.val + left + right
            if total // i == node.val:
                cnt += 1
            print(total)
            return total,i
        aveg(root)
        return cnt