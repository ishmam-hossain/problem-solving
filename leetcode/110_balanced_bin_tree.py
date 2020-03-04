# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_height(root, h=0):
    if root is None:
        return h
    h += 1
    return max(get_height(root.left, h), get_height(root.right, h))


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if abs(get_height(root.left) - get_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


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
print(s.isBalanced(stringToTreeNode("[1,2,2,3,3,null,null,4,4,1,1]")))

