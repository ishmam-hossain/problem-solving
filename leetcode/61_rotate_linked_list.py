# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next

        final = [-1] * len(res)
        for i, n in enumerate(res):
            final[(i+k) % len(res)] = n

        res = ListNode(0)
        cur = res
        for node in final:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = Solution()
print(s.rotateRight(l, 3))
