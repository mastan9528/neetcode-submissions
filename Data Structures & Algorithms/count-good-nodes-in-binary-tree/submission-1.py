# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorder(self , root):
        if not root:
            return

        if len(self.stack) == 0:
            self.stack.append((root.val , root))
            self.count +=1

        elif self.stack and self.stack[-1][0] <= root.val:
            self.stack.append((root.val , root))
            self.count +=1

        self.preorder(root.left)
        self.preorder(root.right)
        if self.stack[-1][1] == root:
            self.stack.pop()

        return



    def goodNodes(self, root: TreeNode) -> int:
        self.stack = []
        self.count = 0

        if not root:
            return self.count

        self.preorder(root)
        return self.count

        