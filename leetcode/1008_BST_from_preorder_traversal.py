import bisect


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if not preorder:
            return

        res = TreeNode(preorder[0])
        i = bisect.bisect(preorder, preorder[0])

        res.left = self.bstFromPreorder(preorder[1:i])
        res.right = self.bstFromPreorder(preorder[i:])

        return res
