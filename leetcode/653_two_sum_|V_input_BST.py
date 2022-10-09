# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def get_nodes(head, nodes):
            if head:
                nodes.append(head.val)
                get_nodes(head.left, nodes)
                get_nodes(head.right, nodes)
            return nodes

        nodes = get_nodes(root, [])

        for ix, i in enumerate(nodes):
            for jx, j in enumerate(nodes):
                if ix != jx and i + j == k:
                    return True
        return False

