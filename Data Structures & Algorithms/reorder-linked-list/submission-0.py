# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # the edge of the slow pointer should be half way of the first
        # while fp.next:
        #     sp = sp.next
        #     fp = fp.next
        #     if fp.next:
        #         fp = fp.next
        fp = sp = head
        while fp.next:
            sp = sp.next
            fp = fp.next
            if fp.next:
                fp = fp.next

        # Reverses the second half
        prev = None
        curr = sp.next
        sp.next = None # splits the list

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # start off with prev, merge two halves
        first, second = head, prev
        while second:
            first_nxt = first.next
            second_nxt = second.next
            
            first.next = second
            second.next = first_nxt

            first = first_nxt
            second = second_nxt
        # n = 1
        # curr = np = head 
        # while np != sp.next:
        #     if n % 2 == 1:
        #         curr.next = prev
        #         prev = prev.next
        #         curr = curr.next
        #     else:
        #         curr.next = np
        #         np   = np.next
        #         curr = curr.next
        #     n += 1
        


            

        
            