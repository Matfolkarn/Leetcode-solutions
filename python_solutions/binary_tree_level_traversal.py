# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        def rec_level(level, node):
            nonlocal res
            if node is None:
                return
            if level > len(res) - 1:
                print(node.val)
                res.append([])
            res[level].append(node.val)

            rec_level(level + 1, node.left)
            rec_level(level + 1, node.right)
        rec_level(0, root)
        return res
