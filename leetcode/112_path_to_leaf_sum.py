# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        if root.val == sum and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, root.val)


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


s = Solution()
print(s.hasPathSum(stringToTreeNode("[5,4,8,11,null,13,4,7,2,null,null,null,1]"), 22))
def hasPathSum(self, root: TreeNode, _sum: int) -> bool:
    def root_to_leaf(node, stack):
        if node is None:
            return
        stack.append(node)
        if node.left is None and node.right is None:
            print([n.val for n in stack], sum([n.val for n in stack]))
            if _sum == sum([n.val for n in stack]):
                return True

        root_to_leaf(node.left, stack)
        root_to_leaf(node.right, stack)
        stack.pop()

        return False

    if not root:
        return False

    return root_to_leaf(root, [])


t = TreeNode(5)
t.left = TreeNode(4)
t.right = TreeNode(8)
t.left.left = TreeNode(11)
t.left.right = TreeNode(2)
t.right.left = TreeNode(1)
t.right.right = TreeNode(3)


s = Solution()
print(s.hasPathSum(t, 22))


"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

                                                      5
                                                     / \
                                                    4   8
                                                   /   / \
                                                  11  13  4
                                                 /  \      \
                                                7    2      1
                                                
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""
