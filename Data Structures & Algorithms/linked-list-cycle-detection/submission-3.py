# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        sp = head # slow pointer
        fp = head.next # faster point
        if not fp:
            return False # check if the next node is not null

        while sp:
            if fp == sp:
                return True

            if sp.next:
                sp = sp.next
            else: 
                return False

            if fp.next:
                fp = fp.next
            else: 
                return False

            if fp.next:
                fp = fp.next
            else: 
                return False


        return False