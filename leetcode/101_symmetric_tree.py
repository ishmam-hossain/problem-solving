# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checker(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return checker(left.left, right.right) and checker(left.right, right.left)

        if root is None:
            return True

        return checker(root.left, root.right)


root_node = TreeNode(1)
root_node.left = TreeNode(2)
root_node.right = TreeNode(2)
root_node.left.left = TreeNode(3)
root_node.right.right = TreeNode(3)
root_node.left.right = TreeNode(4)
root_node.right.left = TreeNode(4)

s = Solution()
print(s.isSymmetric(root_node))


"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
                    
                        1
                       / \
                      2   2
                     / \ / \
                    3  4 4  3
                     

But the following [1,2,2,null,3,null,3] is not:
                    
                        1
                       / \
                      2   2
                       \   \
                       3    3

"""