# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path
            if node is None:
                return 0

            r = max(0, dfs(node.right))
            l = max(0, dfs(node.left))
            p = node.val + r + l
            max_path = max(p, max_path)
            return node.val + max(l,r)
        dfs(root)
        return max_path
