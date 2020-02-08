# Definition for singly-linked list.
from math import log10

class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:
    def get_number(self, ll):
        nxt = ll
        num_list = [nxt.val]
        while nxt.next:
            num_list.append(nxt.next.val)
            nxt = nxt.next

        res = 0
        for i in range(len(num_list)):
            res += num_list[i] * (10 ** (len(num_list) - i - 1))
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode(0)

        res = self.get_number(l1) + self.get_number(l2)
        digits = []
        while res:
            rem = res % 10
            digits.append(rem)
            res = res // 10

        last_node = None
        for digit in digits[::-1]:
            a = ListNode(digit)
            a.next = last_node
            last_node = a
        return a


l1_nxt_2 = ListNode(3)
l1_nxt_1 = ListNode(4, l1_nxt_2)
l1 = ListNode(2, l1_nxt_1)

l2_nxt_2 = ListNode(4)
l2_nxt_1 = ListNode(6, l2_nxt_2)
l2 = ListNode(5, l2_nxt_1)

c = Solution()

data = c.addTwoNumbers(l1, l2)
while data.next:
    print(vars(data.next))
    data = data.next



