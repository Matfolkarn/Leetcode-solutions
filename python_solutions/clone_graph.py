"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old = {}
        def deep_copy(node):
            if node in old:
                return old[node]

            copy = Node(node.val)
            old[node] = copy
            copy.neighbors = [deep_copy(n) for n in node.neighbors]
            return copy           
        return deep_copy(node)  if node else None
