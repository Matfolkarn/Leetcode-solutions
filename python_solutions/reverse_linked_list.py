# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        n = head
        while n is not None:
            n_temp = n.next
            n.next = prev
            prev = n
            n = n_temp
        return prev
