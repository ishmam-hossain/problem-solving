# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def min_depth_recursive(root: TreeNode) -> int:
    def get_min_depth(head, depth=0):
        if head is None:
            return depth
        return get_min_depth(head.left, depth + 1) and get_min_depth(head.right, depth + 1)
    return get_min_depth(root)


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque()
        depth = 1
        q.append(root)

        while q:
            cur = q.popleft()
            if cur.left is None and cur.right is None:
                return depth
            depth += 1
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)


left_9 = TreeNode(9)
right_7 = TreeNode(7)
right_15 = TreeNode(15)
right_20 = TreeNode(20, right_15, right_7)
r = TreeNode(3, left_9, right_20)

r1 = TreeNode(1)
r1.right = TreeNode(2)

r2 = TreeNode(1)

s = Solution()
print(s.minDepth(r))
print(s.minDepth(r1))
print(s.minDepth(r2))

