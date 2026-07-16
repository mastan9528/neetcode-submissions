# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self , p , q):
        if self.flag:
            return False
        if not p and not q:
            return True
        if (not p and q ) or (not q and p):
            self.flag = True
            return False

        if p.val !=q.val:
            self.flag = True
            return False
        self.dfs(p.left ,q.left)
        self.dfs(p.right ,q.right)
        return True 

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = False
        self.dfs(p , q)
        if self.flag:
            return False
        return True