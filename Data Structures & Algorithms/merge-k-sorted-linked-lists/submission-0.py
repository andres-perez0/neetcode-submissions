# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode()
        curr = dummy
        temp_list = []

        while len(lists) > 1:

            n = len(lists)
            for i in range(0, n, 2):
                l1 = lists[i]

                if i + 1 != n:
                    l2 = lists[i+1]
                else:
                    l2 = []
                
                temp_list.append(self.mergeTwoLists(l1, l2))

            lists = temp_list  
            temp_list = []     
              
        return lists[0]