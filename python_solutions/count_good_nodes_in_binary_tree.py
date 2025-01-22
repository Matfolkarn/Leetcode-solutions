# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(max_v, node):
            if node is None:
                return 0
            r = 0
            if node.val >= max_v:
                r = 1
                max_v = node.val
            
            r1 = dfs(max_v, node.left)
            r2 = dfs(max_v, node.right)

            return r1 + r2 + r


        res = dfs(root.val, root)
        return res
