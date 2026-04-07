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
            stack_copy = stack.copy()
            stack = []
            
            for node in stack_copy:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            
        return res
        