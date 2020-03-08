# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.get_depth(root, 0, False)
        right = self.get_depth(root, 0, True)
        return left + right + (1 if left > 0 and right > 0 else 0)

    def get_depth(self, head, depth, min_depth=True):
        if head is None:
            return depth - 1

        if not min_depth:
            return min(self.get_depth(head.left, depth + 1), self.get_depth(head.right, depth + 1))
        else:
            return max(self.get_depth(head.left, depth + 1), self.get_depth(head.right, depth + 1))


t = TreeNode(2)
t.left = TreeNode(3)
t.left.left = TreeNode(1)
# t.left.left = TreeNode(4)
# t.left.right = TreeNode(5)

s = Solution()
print(s.diameterOfBinaryTree(t))

"""
          1
         / \
        2   3
       / \     
      4   5 

[2,3,null,1]
[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
"""