# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root):
        if not root:
            return 0
        if root and root.left is None and root.right is None:
            return 1

        left = 1+ self.dfs(root.left)
        right = 1+self.dfs(root.right)

        return max(left ,right)
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.dfs(root)
        