# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        vals = []

        def get_level_val(head, depth):
            if not head:
                return
            if not head.left and not head.right:
                return head.val, depth

            vals.append(get_level_val(head.left, depth + 1))
            vals.append(get_level_val(head.right, depth + 1))

        if root is None:
            return 0

        get_level_val(root, 1)
        vals = [v for v in vals if v]

        deepest_level = -1
        for i, lvl in enumerate(vals):
            deepest_level = max(deepest_level, lvl[1])

        return sum([v for v, l in vals if l == deepest_level])


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.left.left = TreeNode(7)
tree.left.right = TreeNode(5)
tree.right = TreeNode(3)
tree.right.right = TreeNode(6)
tree.right.right.right = TreeNode(8)

s = Solution()
print(s.deepestLeavesSum(tree))
