class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def iterative_inorder_traversal(self, root: TreeNode):    # -> list[int]:
        if not root:
            return

        stack = [root]
        output = []
        while stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                output.append(root.val)
                root = root.right
            print("stack-->> ", stack)

        return output

    def recursive_inorder_traversal(self, root: TreeNode):    # -> list[int]:
        output = []
        if root:
            output.extend(self.recursive_inorder_traversal(root.left))
            output.append(root.val)
            output.extend(self.recursive_inorder_traversal(root.right))
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
print(s.iterative_inorder_traversal(f_root))
print(s.recursive_inorder_traversal(f_root))

# TODO --> solution -->     A B C D E F G H I
"""
    first root
    then left sub-tree
    then right sub-tree
"""
