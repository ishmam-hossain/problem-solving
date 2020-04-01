# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        original = []
        cur = head
        while cur:
            original.append(cur.val)
            cur = cur.next

        reverse = [*original[:m-1], *original[m-1:n][::-1], *original[n:]]

        res = ListNode(0)
        cur = res
        for node in reverse:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next



l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
# l.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.reverseBetween(l, 2, 4))
