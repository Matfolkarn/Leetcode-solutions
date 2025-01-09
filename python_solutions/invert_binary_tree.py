# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def rec_inv(node):
            if node == None:
                return
            right_temp = node.right
            node.right = node.left
            node.left = right_temp
            rec_inv(node.right)
            rec_inv(node.left)

        rec_inv(root)
        return root
