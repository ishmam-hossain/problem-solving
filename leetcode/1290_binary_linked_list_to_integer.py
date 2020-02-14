# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next

        dec_number = 0
        for i, n in enumerate(res[::-1]):
            dec_number += n * 2 ** i

        return dec_number


l1_nxt_2 = ListNode(0)
l1_nxt_1 = ListNode(0, l1_nxt_2)
l1_nxt_3 = ListNode(1, l1_nxt_1)
l1 = ListNode(1, l1_nxt_3)

c = Solution()
data = c.getDecimalValue(l1)
data = c.add_linked_list(l1)
print(data)

a = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
