# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.total = 0

        def count_nodes(head):
            if head is None:
                return
            self.total += 1
            count_nodes(head.left)
            count_nodes(head.right)

        count_nodes(root)

        return self.total