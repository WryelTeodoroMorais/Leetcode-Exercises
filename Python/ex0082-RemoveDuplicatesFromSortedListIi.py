# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        lista = ListNode(0, head)
        aux = head
        temp = lista
        while aux:
            if aux.next and aux.val == aux.next.val:
                val = aux.val
                while aux and aux.val == val:
                    aux = aux.next
                temp.next = aux
            else:
                temp = aux
                aux = aux.next
        return lista.next