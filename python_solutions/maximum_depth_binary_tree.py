# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(node, depth):
            if node == None:
                return depth
            else: 
                new_depth = depth + 1
                return max(max_depth(node.right, new_depth), max_depth(node.left, new_depth))
        return max_depth(root,0)
      
