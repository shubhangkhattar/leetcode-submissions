# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode()
        head = prev
        carry = 0
        while l1 or l2:
            new_node = ListNode()
            prev.next = new_node
            prev = new_node
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            new_node.val = carry % 10
            carry = carry // 10
        
        if carry:
            new_node = ListNode(carry)
            prev.next = new_node

        return head.next
