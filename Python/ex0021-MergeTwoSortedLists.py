# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        aux1, aux2 = list1, list2
        result = ListNode()
        temp = result
        while aux1 and aux2:
            if aux1.val <= aux2.val:
                temp.next = aux1 
                temp = temp.next 
                aux1 = aux1.next
            else:
                temp.next = aux2
                temp = temp.next
                aux2 = aux2.next

        if aux1:
            temp.next = aux1 
        elif aux2:
            temp.next = aux2

        return result.next
        