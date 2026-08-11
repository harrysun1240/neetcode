# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = last = ListNode()
        while head:
            start = head
            for i in range(k - 1):
                head = head.next
                if head == None:
                    return dummy.next
            end = head
            head = head.next
            end.next = None

            curr = start
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            last.next = prev
            start.next = head
            last = start
        return dummy.next
