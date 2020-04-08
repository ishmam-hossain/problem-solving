# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def better_solution(self, head):
        tot = 0
        cur = head
        while cur:
            tot += 1
            cur = cur.next

        mid = (tot // 2) + 1

        cur = head
        pos = 1
        while cur:
            if pos == mid:
                return cur
            cur = cur.next
            pos += 1

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