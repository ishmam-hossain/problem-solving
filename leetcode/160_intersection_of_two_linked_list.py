# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = set()

        cur = headA
        while cur:
            a.add(cur)
            cur = cur.next

        cur = headB
        while cur:
            if cur in a:
                return cur
            cur = cur.next

        return