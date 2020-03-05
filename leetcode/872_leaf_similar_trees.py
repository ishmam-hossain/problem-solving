# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = self.helper(root1, [])
        l2 = self.helper(root2, [])

        return l1 == l2

    def helper(self, head, leaves):
        if head is None:
            return
        if not head.left and not head.right:
            leaves.append(head.val)

        self.helper(head.left, leaves)
        self.helper(head.right, leaves)

        return leaves
