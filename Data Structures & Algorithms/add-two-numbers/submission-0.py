# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        power, n1 = 0, 0
        while l1:
            n1 += l1.val * 10 ** power
            power += 1
            l1 = l1.next
        power, n2 = 0, 0
        while l2:
            n2 += l2.val * 10 ** power
            power += 1
            l2 = l2.next
        
        n = n1 + n2
        dummy = res = ListNode()
        if n == 0:
            return dummy
        while n:
            res.next = ListNode(n % 10)
            res = res.next
            n //= 10
        
        return dummy.next
