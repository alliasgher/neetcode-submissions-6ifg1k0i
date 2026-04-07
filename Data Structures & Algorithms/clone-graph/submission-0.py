"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(n):
            if n in oldtonew:
                return oldtonew[n]

            copy = Node(n.val)
            oldtonew[n] = copy
            

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return oldtonew[n]

        if not node:
            return None
        return dfs(node)
                

        