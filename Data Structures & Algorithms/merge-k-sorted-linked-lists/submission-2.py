# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self,list1,list2):
        
        dummy = ListNode()
        head = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            
            head = head.next

        if list1:
            head.next = list1
        
        if list2:
            head.next = list2


        return dummy.next



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return

        while len(lists) != 1:
            
            list1 = lists.pop()
            list2 = lists.pop()

            lists.append(self.merge(list1,list2))

        return lists[-1]

