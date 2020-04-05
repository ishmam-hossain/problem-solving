# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def find_path(l, t):
            if not l:
                return True
            if not t:
                return False

            return t.val == l.val and (find_path(l.next, t.left) or find_path(l.next, t.right))

        if not head:
            return True
        if not root:
            return False

        return find_path(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
