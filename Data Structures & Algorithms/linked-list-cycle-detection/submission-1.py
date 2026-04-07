# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        l = head
        while l:
            if l in visited:
                return True
            visited.add(l)
            l = l.next
        return False
        