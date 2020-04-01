# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []

        def inorder(head):
            if head is None:
                return
            inorder(head.left)
            res.append(head.val)
            inorder(head.right)

        inorder(root)
        final = TreeNode(res[0])
        cur = final
        for node in res[1:]:
            cur.right = TreeNode(node)
            cur = cur.right

        return final


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left.left = TreeNode(1)

tree.right = TreeNode(6)
tree.right.right = TreeNode(8)
tree.right.right.right = TreeNode(9)
tree.right.right.left = TreeNode(7)
tree.right.right.right.right = TreeNode(19)

s = Solution()
data = s.increasingBST(tree)

while data:
    print(data.val)
    data = data.right


"""
                       5
                      / \
                    3    6
                   / \    \
                  2   4    8
                 /        / \ 
                1        7   9

"""