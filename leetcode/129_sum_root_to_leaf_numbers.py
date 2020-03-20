# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def get_sum(head, cur):
            if head is None:
                return 0
            if head.left is None and head.right is None:
                return (cur * 10) + head.val
            return get_sum(head.left, cur * 10 + head.val) + get_sum(head.right, cur * 10 + head.val)

        return get_sum(root, 0)


t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.right = TreeNode(1)

s = Solution()
print(s.sumNumbers(None))
