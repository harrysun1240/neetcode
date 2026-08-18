# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if (not root.left) and (not root.right):
            return 0
        elif (not root.left) and root.right:
            return max(1 + self.maxDepth(root.right), self.diameterOfBinaryTree(root.right))
        elif root.left and (not root.right):
            return max(1 + self.maxDepth(root.left), self.diameterOfBinaryTree(root.left))
        else:
            return max(
                2 + self.maxDepth(root.left) + self.maxDepth(root.right),
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right),
            )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
