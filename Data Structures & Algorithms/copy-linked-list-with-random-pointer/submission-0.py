"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tracer = head
        hash_table = {}

        while tracer:
            # creates an index-able hashmap for a list of nodes
            hash_table[tracer] = Node(tracer.val, None, None)
            # increments everything ahead by one
            tracer = tracer.next

        tracer = head # reset the position
        curr = Node(0, None, None) # val, nxt, rdm
        new_head = curr

        while tracer:
            curr.next = hash_table[tracer]
            curr = curr.next

            if tracer.random:
                curr.random = hash_table[tracer.random]

            tracer = tracer.next

        return new_head.next
        