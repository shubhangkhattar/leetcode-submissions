# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        head_1 = head
        head_2 = self.reverseList(slow.next)
        slow.next = None
        prev = None

        while head_2:
            tmp_1, tmp_2 = head_1.next, head_2.next
            
            head_1.next = head_2
            head_2.next = tmp_1

            head_1 = tmp_1
            head_2 = tmp_2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while (head):
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev