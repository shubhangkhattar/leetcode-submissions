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
        
        myMap = {None:None}
        cur = head
        while head:
            myMap[head] = Node(head.val) 
            head = head.next
        
        head = cur
        while head:
            myMap[head].next = myMap[head.next]
            myMap[head].random = myMap[head.random]
            head = head.next
        
        return myMap[cur]
            