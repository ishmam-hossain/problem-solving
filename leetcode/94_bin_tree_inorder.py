# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []

        def inorder(head):
            if head is None:
                return

            inorder(head.left)
            nodes.append(head.val)
            inorder(head.right)

        inorder(root)
        return nodes