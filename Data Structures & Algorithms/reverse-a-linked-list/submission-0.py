# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            node = curr.next # saves the next one
            curr.next = prev # the curr points to the previous node
            prev = curr      # moves the prev node to the current node     
            curr = node      # moves the curr node to the saved next one

        return prev