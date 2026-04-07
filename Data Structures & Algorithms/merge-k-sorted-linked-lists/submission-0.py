# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        #divide and conquer
        #first divide lists into pairs of two and keep merging each 
        #pair until it becomes one
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergedList.append(self.mergeTwo(l1, l2))
            lists = mergedList
        return lists[0]

    def mergeTwo(self, l1, l2):
        dummy = ListNode(0)
        start = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                start.next = l1
                l1 = l1.next
            else:
                start.next = l2
                l2 = l2.next
            start = start.next

        if l1:
            start.next = l1
        elif l2:
            start.next = l2
        return dummy.next
                

