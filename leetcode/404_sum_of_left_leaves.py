# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leaf_sum = 0
        if root is None:
            return leaf_sum
        if root.left is not None and root.left.left is None and root.left.right is None:
            leaf_sum += root.left.val

        leaf_sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return leaf_sum


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

s = Solution()
print(s.sumOfLeftLeaves(t))

"""
    3
   / \
  9  20
    /  \
   15   7
"""