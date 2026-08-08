# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        front, back = head, prev
        while back:
            temp1 = front.next
            front.next = back
            temp2 = back.next
            back.next = temp1
            front, back = temp1, temp2
