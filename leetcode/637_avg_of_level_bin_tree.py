# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_dict = dict()

        def get_level_dict(node, level):
            if node is None:
                return

            level_dict.setdefault(level, []).append(node.val)

            get_level_dict(node.left, level + 1)
            get_level_dict(node.right, level + 1)

        get_level_dict(root, 1)
        return [sum(item) / len(item) for item in level_dict.values()]
