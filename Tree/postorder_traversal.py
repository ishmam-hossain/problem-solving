class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def iterative_postorder_traversal(self, root: TreeNode):    # -> list[int]:
        if not root:
            return

        stack = [root]
        output = []
        while stack:
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
            output.append(root.val)
            root = stack.pop()

        return output

    def recursive_postorder_traversal(self, root: TreeNode):    # -> list[int]:
        output = []
        if root:
            output.extend(self.recursive_postorder_traversal(root.left))
            output.extend(self.recursive_postorder_traversal(root.right))
            output.append(root.val)
        return output


a = TreeNode('A')
c = TreeNode('C')
e = TreeNode('E')
d = TreeNode('D', c, e)
b = TreeNode('B', a, d)
h = TreeNode('H')
i = TreeNode('I', left=h)
g = TreeNode('G', right=i)
f_root = TreeNode('F', b, g)


s = Solution()
print(s.iterative_postorder_traversal(f_root))
print(s.recursive_postorder_traversal(f_root))

# TODO --> solution -->     A C E D B H I G F
"""
    first root
    then left sub-tree
    then right sub-tree
"""
