# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        all_path = []

        def make_path(head, path):
            if head is None:
                return

            path.append(str(head.val))

            if head.left is None and head.right is None:
                all_path.append("->".join(path))
                path.pop()
                return

            make_path(head.left, path)
            make_path(head.right, path)
            path.pop()

        make_path(root, [])

        return all_path
