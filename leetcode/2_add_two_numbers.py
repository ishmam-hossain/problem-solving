class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _carry = 0
        res_node = ListNode(0)
        cur_node = res_node

        while l1 is not None and l2 is not None:
            _sum = l1.val + l2.val + _carry
            _val = _sum % 10
            _carry = _sum // 10
            cur_node.next = ListNode(_val)
            cur_node = cur_node.next
            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            while l1 is not None:
                _sum = l1.val + _carry
                _val = _sum % 10
                _carry = _sum // 10
                cur_node.next = ListNode(_val)
                cur_node = cur_node.next
                l1 = l1.next
        if l2 is not None:
            while l2 is not None:
                _sum = l2.val + _carry
                _val = _sum % 10
                _carry = _sum // 10
                cur_node.next = ListNode(_val)
                cur_node = cur_node.next
                l2 = l2.next

        if l1 is None and l2 is None and _carry:
            cur_node.next = ListNode(_carry)

        return res_node.next

    def new_solution(self, l1, l2):
        carry = 0
        head = ListNode(0)
        cur = head

        while l1 or l2:
            if l1 and l2:
                node_sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l2:
                node_sum = l1.val + carry
                l1 = l1.next
            elif not l1:
                node_sum = l2.val + carry
                l2 = l2.next

            carry = node_sum // 10
            val = node_sum % 10
            cur.next = ListNode(val)
            cur = cur.next

        cur.next = ListNode(carry) if carry else None
        return head.next


def PRINT(d):
    if d is None:
        return
    PRINT(d.next)
    print('-> ', end='')
    print(d.val, end=' ')


l1_nxt_1 = ListNode(9)
ll1 = ListNode(9, l1_nxt_1)

ll2 = ListNode(1)

c = Solution()
PRINT(c.addTwoNumbers(ll1, ll2))
PRINT(c.new_solution(ll1, ll2))



