# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0, None)
        curr = head
        while l1 and l2:
            
            curr_digit_1 = l1.val + carry
            curr_digit_2 = l2.val

            total = curr_digit_1 + curr_digit_2
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            curr.next = ListNode(total, None)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_digit_1 = l1.val + carry
            print(l1.val)
            print(curr_digit_1)
            if curr_digit_1 > 9:
                carry = 1
                curr_digit_1 -= 10
            else:
                carry = 0

            curr.next = ListNode(curr_digit_1, None)
            curr = curr.next

            l1 = l1.next

        while l2:
            curr_digit_2 = l2.val + carry

            if curr_digit_2 > 9:
                carry = 1
                curr_digit_2 -= 10
            else:
                carry = 0

            curr.next = ListNode(curr_digit_2, None)
            curr = curr.next

            l2 = l2.next  

        if carry:
            curr.next = ListNode(1, None)
            curr = curr.next

        return head.next