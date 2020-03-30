# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int):
        class Solution:
            def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
                res = {}
                self.target_level = -1

                def get_nodes(head, depth, is_left):
                    if head is None:
                        return

                    res.setdefault(depth, []).append(head.val)
                    if head.val == target:
                        self.target_level = depth

                    get_nodes(head.left, depth + (-1 if is_left else 1), is_left)
                    get_nodes(head.right, depth + (-1 if is_left else 1), is_left)

                get_nodes(root.left, -1, is_left=True)
                get_nodes(root.right, 1, is_left=False)

                final = []
                for key, val in res.items():
                    if key < 0 and self.target_level < 0:
                        diff = abs(abs(key) - abs(self.target_level))
                    else:
                        diff = abs(key - self.target_level)
                    if diff == K:
                        final.extend(val)
                return final

        # final = [val for key, temp in res.items() if abs(key-self.target_level) == K for val in temp]


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)

s = Solution()
print(s.distanceK(tree, 5, 2))
