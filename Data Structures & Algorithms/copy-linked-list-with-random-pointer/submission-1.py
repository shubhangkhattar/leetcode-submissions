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
        
        my_map = {}

        dummy = head

        while head:
            my_map[head] = Node(head.val)
            head = head.next
        
        head = dummy

        while head:
            next = head.next
            random = head.random
            if next:
                my_map[head].next = my_map[next]
            if random:
                my_map[head].random = my_map[random]
            head = head.next

        return my_map[dummy] if dummy else None

