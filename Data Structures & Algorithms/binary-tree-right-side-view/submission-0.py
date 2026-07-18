# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        li =[]

        if not root:
            return []

        queue = deque([root])
        while queue:

            temp = []
            size = len(queue)

            while size > 0:
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -=1

            li.append(temp)
        res = []
        for item in li:
            res.append(item[-1])

        return res
