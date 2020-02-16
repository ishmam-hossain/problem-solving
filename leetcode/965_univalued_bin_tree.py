# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return False

        val = root.val
        s = [root]
        visited = [root]
        while s:
            node = s.pop()
            if node.val != val:
                return False
            if node.left is not None and node.left not in visited:
                s.append(node.left)
            if node.right is not None and node.right not in visited:
                s.append(node.right)

        return True


t = TreeNode(1)
t.left = TreeNode(12)
t.right = TreeNode(1)

_s = Solution()
print(_s.isUnivalTree(t))
