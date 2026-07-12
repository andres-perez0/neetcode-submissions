# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, start, stop):
        if not start:
            return None

        prev = None
        # prev = start
        curr = start

        while curr != stop:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        global_head = head
        prev_group_tail = None
        curr = head
        index = 0
        while curr:
            
            if index % k == 0:
                start = curr

            if index % k == (k - 1):
                nxt = curr.next # my main idea of originally trying to use end as the limit
                reversed_head = self.reverseLL(start, nxt) 

                if prev_group_tail:
                    prev_group_tail.next = reversed_head
                
                prev_group_tail = start 

                if index == k - 1:
                    global_head = reversed_head

                start.next = nxt
                curr = start

            curr = curr.next
            index += 1

        return global_head
        