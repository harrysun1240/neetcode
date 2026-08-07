# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None

        res = temp = ListNode(0, None)
        curr1, curr2 = list1, list2
        while not (curr1 == None and curr2 == None):
            if curr1 == None:
                res.next = curr2
                curr2 = curr2.next
                res = res.next
                continue
            elif curr2 == None:
                res.next = curr1
                curr1 = curr1.next
                res = res.next
                continue

            if curr1.val <= curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            res = res.next
        return temp.next
