# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #brute force:
        # cur = head
        # nodes = []
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next

        # left = 0
        # right = len(nodes)-1
        
        # while left < right:
        #     nodes[left].next = nodes[right]
        #     nodes[right].next = nodes[left+1]
        #     left+= 1
        #     right -= 1
        # nodes[left].next = None

        #no extra memory:
        #find half using fast and slow

        slow ,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second list
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        #merge both lists
        while head and prev:
            tmp = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp
            head = tmp
            prev = tmp2
        
        print(head)

        
        

        
        