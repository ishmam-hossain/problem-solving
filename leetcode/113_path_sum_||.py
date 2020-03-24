# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, _sum: int):
        all_paths = []

        def get_paths(head, path):
            if head is None:
                return

            path.append(head.val)

            if not head.left and not head.right:
                if sum(path) == _sum:
                    all_paths.append(path[:])

            get_paths(head.left, path)
            get_paths(head.right, path)

            path.pop()

        get_paths(root, [])
        return all_paths


t = TreeNode(5)
t.left = TreeNode(4)
t.right = TreeNode(8)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.left = TreeNode(5)
t.right.right.right = TreeNode(1)

s = Solution()
print(s.pathSum(t, 22))
