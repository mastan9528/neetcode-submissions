# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = False

        def dfs(root):
            if not root:
                return 0
            if self.flag:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            x = left - right
            if x>=2 or x<=-2:
                self.flag = True

            return 1+max(left , right)

        dfs(root)
        if self.flag:
            return False

        return True
        