# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        aux = head
        while aux.next:
            if aux.val == aux.next.val:
                aux.next = aux.next.next
            else:
                aux = aux.next
        
        return head