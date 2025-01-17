# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = True

        def rec_same(p,q):
            nonlocal result
            if p is None and q is None:
                return
            elif p is None or q is None:
                result = False
                return
            if p.val != q.val:
                result = False
            rec_same(p.left, q.left)
            rec_same(p.right, q.right)
        rec_same(p,q)
        return result
