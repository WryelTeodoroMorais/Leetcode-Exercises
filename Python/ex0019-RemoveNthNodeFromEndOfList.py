# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux, cont = head, 0
        while aux:
            aux = aux.next
            cont+=1
        if cont == n:
            return head.next
        index = cont - n
        aux = head
        while index > 0:
            if aux.next and index == 1:
                aux.next = aux.next.next
                break
            else:
                aux = aux.next
                index-=1

        return head