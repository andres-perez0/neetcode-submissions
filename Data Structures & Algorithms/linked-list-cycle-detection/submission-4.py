# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        sp = fp = head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

            if fp == sp:
                return True

        return False