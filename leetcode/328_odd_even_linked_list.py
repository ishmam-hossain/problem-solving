# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next

        res = ListNode(0)
        cur = res
        for i, node in enumerate(nodes, 1):
            if i % 2 != 0:
                cur.next = ListNode(node)
                cur = cur.next

        for i, node in enumerate(nodes, 1):
            if i % 2 == 0:
                cur.next = ListNode(node)
                cur = cur.next

        return res.next
