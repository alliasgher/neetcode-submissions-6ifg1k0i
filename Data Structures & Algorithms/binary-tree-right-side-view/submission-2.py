# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            r = stack[-1]
            res.append(r.val)
            next_stack = []
            
            for node in stack:
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            stack = next_stack

            
        return res
        