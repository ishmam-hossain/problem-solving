# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque()
        depth = 1
        q.append({'node': root, 'depth': depth})

        while q:
            cur = q.popleft()
            depth = cur['depth']
            node = cur['node']
            if node.left is None and node.right is None:
                return depth
            if node.left is not None:
                q.append({'node': node.left, 'depth': depth+1})
            if node.right is not None:
                q.append({'node': node.right, 'depth': depth+1})

    def min_depth_recursive(self, root):
        def get_depth(head, depth):
            if head is None:
                return depth
            return min(get_depth(head.left, depth+1), get_depth(head.right, depth+1))

        return get_depth(root, 0)


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)
t.right = TreeNode(4)

s = Solution()
print(s.min_depth_recursive(t))
