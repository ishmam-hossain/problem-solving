# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def iterative_preorder_traversal(self, root: TreeNode):    # -> list[int]:
        if not root:
            return

        stack = [root]
        output = []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

        return output

    def recursive_preorder_traversal(self, root: TreeNode):    # -> list[int]:
        output = []
        if root:
            output.append(root.val)
            output.extend(self.recursive_preorder_traversal(root.left))
            output.extend(self.recursive_preorder_traversal(root.right))

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
print(s.iterative_preorder_traversal(f_root))
print(s.recursive_preorder_traversal(f_root))

# TODO --> solution --> F B A D C E G I H
"""
    first root
    then left sub-tree
    then right sub-tree
"""
