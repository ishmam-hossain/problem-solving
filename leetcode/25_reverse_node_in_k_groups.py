# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nodes = []

        cur = head
        while cur:
            nodes.append(cur.val)
            cur = cur.next

        reverted = [nodes[i:i+k][::-1] if i+k <= len(nodes) else nodes[i:i+k] for i in range(0, len(nodes), k)]
        final = [val for temp in reverted for val in temp]

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
l.next.next.next.next.next = ListNode(6)


s = Solution()
data = s.reverseKGroup(l, 3)

while data:
    print(data.val, end=" ")
    data = data.next
