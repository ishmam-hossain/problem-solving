# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def get_sum(node, res):
            if node is None:
                return

            if L <= node.val <= R:
                res.append(node.val)
            get_sum(node.left, res)
            get_sum(node.right, res)

            return res

        return sum(get_sum(root, []))


tree_node = TreeNode(10)
tree_node.left = TreeNode(5)
tree_node.right = TreeNode(15)
tree_node.left.left = TreeNode(3)
tree_node.left.right = TreeNode(7)
tree_node.left.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(tree_node, 7, 15))


"""
                            10
                        5        15
                     3     7  
                              18      

"""