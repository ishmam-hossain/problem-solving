# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def get_nodes(node):
            if node:
                get_nodes(node.left)
                res.append(node.val)
                get_nodes(node.right)

        get_nodes(root1)
        get_nodes(root2)
        res.sort()
        return res