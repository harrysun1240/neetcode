"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        dummy = res = Node(0)
        nodes = {}

        while curr:
            res.next = nodes[curr] = Node(curr.val, None, None)
            res = res.next
            curr = curr.next

        res = dummy
        while head:
            res.next.random = nodes[head.random] if head.random else None
            res = res.next
            head = head.next

        return dummy.next
