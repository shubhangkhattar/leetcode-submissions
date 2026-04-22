# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self,node):
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        first = head
        second = head

        while second.next and second.next.next:
            second = second.next.next
            first = first.next

        second = first.next
        first.next = None
        
        second = self.reverse(second)
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            second = temp2
            first = temp1
        


        

        #    t

        # 0 > 1 > 2 > 3
        # f

        # 7 > 6 > 5 > 4
        # s             