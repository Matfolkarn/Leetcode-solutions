# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def rec(node):
            if max(p.val, q.val) < node.val:
                return rec(node.left)
            elif min(p.val, q.val) > node.val:
                return rec(node.right)
            else:
                return node
        res = rec(root)
        return res
