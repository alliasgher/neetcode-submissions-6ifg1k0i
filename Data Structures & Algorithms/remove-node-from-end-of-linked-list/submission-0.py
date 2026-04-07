# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        
        #set right to left+n
        while n>0:
            right = right.next
            n -= 1
        
        #edge case: when head needs to be removed
        #we can either use dummy at start for this or check manually
        if not right:
            return head.next

        tmp = left
        #move pointers until right is at end of list so left is at end-n
        while right:
            tmp = left
            left = left.next
            right = right.next

        tmp.next = left.next
        return head