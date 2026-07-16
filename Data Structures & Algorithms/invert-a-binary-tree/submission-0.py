# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if not root:
            return
        if root and root.left is None and root.right is None:
            return root 
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)
        