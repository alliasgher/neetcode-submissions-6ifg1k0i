# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive
        # def traverse(node):
        #     if not node:
        #         return None
        
        #     traverse(node.left)
        #     arr.append(node.val)
        #     traverse(node.right)

        # arr = []
        # traverse(root)
        # return arr[k-1]


        #iterative
        res = [root]
        cur = root

        if not root:
            return None

        while cur or res:
            while cur:
                res.append(cur)
                cur = cur.left

            node = res.pop()
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                cur = node.right
            
        
            

        