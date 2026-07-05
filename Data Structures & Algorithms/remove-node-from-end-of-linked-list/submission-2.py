# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        rm_ptr = st_ptr = dummy

        while n > 0 and st_ptr.next:
            st_ptr = st_ptr.next
            n -= 1
        # if st_ptr == rm_ptr:
        #     return None

        while st_ptr.next:
            st_ptr = st_ptr.next
            rm_ptr = rm_ptr.next

        # if rm_ptr == head and st_ptr.next:
        #     if head.next:
        #         head = head.next
        #     else:
        #         return None
        # else:
        rm_ptr.next = rm_ptr.next.next

        return dummy.next
        
        