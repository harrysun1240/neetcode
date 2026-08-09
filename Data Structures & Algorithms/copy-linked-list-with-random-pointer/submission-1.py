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
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None
        curr = head
        while curr:
            nodes[curr].val = curr.val
            nodes[curr].next = nodes[curr.next]
            nodes[curr].random = nodes[curr.random]
            curr = curr.next
        return nodes[head]
