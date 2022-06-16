# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view_nodes = []
        visited_levels = set()

        def right_view(node, level=0):
            if node is None:
                return []
            if level not in visited_levels:
                right_view_nodes.append(node.val)
                visited_levels.add(level)
            right_view(node.right, level+1)
            right_view(node.left, level+1)
        right_view(root, level=0)
        return right_view_nodes
