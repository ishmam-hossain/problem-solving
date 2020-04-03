# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.final = 0
        def max_depth(head):
            if head is None:
                return 0
            left, right = max_depth(head.left), max_depth(head.right)
            self.final = max(self.final, left+right)
            return max(left, right) + 1
        max_depth(root)
        return self.final


