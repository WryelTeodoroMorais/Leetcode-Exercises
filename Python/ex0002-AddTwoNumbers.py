# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result1, result2 = [], []
        current1, current2 = l1, l2
        while current1:
            result1.append(current1.val)
            current1 = current1.next
        while current2:
            result2.append(current2.val)
            current2 = current2.next

        soma = int(''.join(str(x) for x in result1[::-1])) + int(''.join(str(y) for y in result2[::-1]))
        aux = str(soma)
        head = None
        for i in aux:
            head = ListNode(int(i), head)

        return head