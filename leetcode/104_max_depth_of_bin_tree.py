# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(head, depth=0):
            if head is None:
                return depth
            return max(get_depth(head.right, depth+1), get_depth(head.left, depth+1))

        return get_depth(root)
