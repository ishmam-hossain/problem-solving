# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def print_path(stack, root, final):
            if root is None:
                return
            stack.append(root)
            if root.left is None and root.right is None:
                final.append(int("".join([str(n.val) for n in stack]), 2))

            print_path(stack, root.left, final)
            print_path(stack, root.right, final)
            stack.pop()

            return sum(final)
        if root is None:
            return 0
        return print_path([], root, [])


t = TreeNode(1)
t.left = TreeNode(0)
t.left.left = TreeNode(0)
t.left.right = TreeNode(1)
t.right = TreeNode(1)
t.right.left = TreeNode(0)
t.right.right = TreeNode(1)


s = Solution()
print(s.sumRootToLeaf(t))
