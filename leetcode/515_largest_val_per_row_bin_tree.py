# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        all_vals = {}

        def level_order(head, depth):
            if head is None:
                return
            depth += 1
            all_vals.setdefault(depth, []).append(head.val)

            level_order(head.left, depth)
            level_order(head.right, depth)

        level_order(root, 0)

        return [max(val) for val in all_vals.values()]

