# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def building(self , left_value , right_value , preorder , dic):
        if left_value > right_value or self.itr >= len(preorder):
            return
        index = preorder[self.itr]
        new_node = TreeNode(preorder[self.itr])
        self.itr += 1
        new_node.left = self.building(left_value , dic[index]-1 , preorder , dic )
        new_node.right= self.building(dic[index]+1 , right_value , preorder , dic)
        return new_node

        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.itr = 0
        dic = {}
        # if len(inorder) == 1:
        #     new_node = TreeNode(inorder[0])
        #     return new_node

        for i in range(len(inorder)):
            dic[inorder[i]] = i

        return self.building(0,len(preorder) , preorder ,dic)
        