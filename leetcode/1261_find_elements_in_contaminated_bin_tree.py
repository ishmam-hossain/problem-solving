# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = set()

        def fix_tree(head):
            if head is None:
                return
            if head.left is not None:
                val = (head.val * 2) + 1
                head.left.val = val
                self.elements.add(val)
            if head.right is not None:
                val = (head.val * 2) + 2
                head.right.val = val
                self.elements.add(val)

            fix_tree(head.left)
            fix_tree(head.right)

        root.val = 0
        fix_tree(root)

    def find(self, target: int) -> bool:
        return target in self.elements

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
