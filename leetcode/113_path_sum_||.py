# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        def find_path(head, cur_path, _s):
            if head is None:
                return

            cur_path.append(head.val)

            if head.val == _s and head.left is None and head.right is None:
                paths.append(cur_path)
                # cur_path.pop()
                return
            else:
                find_path(head.left, cur_path, _s - head.val)
                find_path(head.right, cur_path, _s - head.val)

            cur_path.pop()

        paths = []
        find_path(root, [], sum)
        return paths


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
