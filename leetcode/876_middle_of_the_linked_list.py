# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tot = 0
        cur = head
        res = []
        while cur:
            tot += 1
            res.append(cur)
            cur = cur.next

        mid = (tot // 2)

        return res[mid]