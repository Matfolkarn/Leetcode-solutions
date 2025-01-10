# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = True
        def dfs(node):
            nonlocal balanced

            if not node:
                return 0
            right_dep = dfs(node.right)
            left_dep = dfs(node.left)

            if right_dep - left_dep > 1 or right_dep - left_dep < - 1:
                balanced = False
            return 1 + max(right_dep, left_dep)

        dfs(root)
        return balanced
