# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        vals = {}

        def level(head, depth):
            if head is None:
                return
            vals.setdefault(depth, []).append(head.val)
            level(head.left, depth + 1)
            level(head.right, depth + 1)

        level(root, 1)
        res = []
        for v in reversed(vals.values()):
            res.append(v)
        return res