# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.constructBST(nums, 0, len(nums) - 1)

    def constructBST(self, arr, left, right):
        if left > right:
            return

        mid = (left + right) // 2
        node = TreeNode(arr[mid])
        node.left = self.constructBST(arr, left, mid - 1)
        node.right = self.constructBST(arr, mid + 1, right)

        return node
