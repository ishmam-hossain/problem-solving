# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res = {}

        def level_order(head, depth):
            if head is None:
                return depth - 1
            res.setdefault(depth, []).append(head.val)

            level_order(head.left, depth + 1)
            level_order(head.right, depth + 1)

        level_order(root, 1)
        temp = {key: sum(val) for key, val in res.items()}
        max_sum = max(temp.values())
        temp = {key: val for key, val in temp.items() if val == max_sum}

        return min(temp.keys())
