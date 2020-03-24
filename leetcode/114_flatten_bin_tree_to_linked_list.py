# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        res = []

        def make_linked_list(head):
            if head is None:
                return

            res.append(head)

            make_linked_list(head.left)
            make_linked_list(head.right)

        make_linked_list(root)
        final = res[0]
        cur = final
        for node in res[1:]:
            cur.right = node
            cur = cur.right

        return final



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(5)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.right.right = TreeNode(6)

s = Solution()
x = s.flatten(tree)

while x:
    print(x.val)
    x = x.right

"""
                                    1
                                   / \
                                  2   5
                                 / \   \
                                3   4   6

"""