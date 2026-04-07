# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, curMax):
            if not node:
                return 0

            if node.val >= curMax:
                curMax = node.val
                return 1 + dfs(node.left, curMax) + dfs(node.right, curMax)
            
            else:
                return dfs(node.left, curMax) + dfs(node.right, curMax)

        return dfs(root, root.val -1)
        

            

            
        