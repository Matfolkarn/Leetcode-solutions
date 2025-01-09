# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:    
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow
        l2_next = l2.next
        l2.next = None
        while l2_next:
            l2_temp = l2_next.next
            l2_next.next = l2
            l2 = l2_next
            l2_next = l2_temp
        l1 = head
        while l2.next:
            l1_next = l1.next
            l1.next = l2
            l1 = l1_next
            l2_next = l2.next
            l2.next = l1_next
            l2 = l2_next
            
