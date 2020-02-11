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


def PRINT(d):
    if d is None:
        return
    PRINT(d.next)
    print('-> ', end='')
    print(d.val, end=' ')


def get_digits(linked_list, out):
    if linked_list is None:
        return
    out.append(linked_list.val)
    get_digits(linked_list.next, out)
    return out


def reverse_linked_list(ll):
    return ll[::-1]


def new_add_test(ll1, ll2):
    n1 = get_digits(ll1, [])
    n2 = get_digits(ll2, [])

    n = max(len(n1), len(n2))
    _carry = 0
    res = []
    new_node = None
    prev_node = None
    for i in range(n):
        local_sum = n1[i] + n2[i] + _carry
        _carry = local_sum // 10
        res.append(local_sum % 10)
        new_node = ListNode(local_sum % 10)
        new_node.next = prev_node
        prev_node = new_node

    return new_node


l1_nxt_2 = ListNode(3)
l1_nxt_1 = ListNode(4, l1_nxt_2)
l1 = ListNode(2, l1_nxt_1)

l2_nxt_2 = ListNode(4)
l2_nxt_1 = ListNode(6, l2_nxt_2)
l2 = ListNode(5, l2_nxt_1)

# c = Solution()
# data = c.addTwoNumbers(l1, l2)
# print(PRINT(data))
PRINT(new_add_test(l1, l2))


