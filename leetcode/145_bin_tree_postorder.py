# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def do_post(head):
            if head is None:
                return
            do_post(head.left)
            do_post(head.right)
            res.append(head.val)

        do_post(root)

        return res