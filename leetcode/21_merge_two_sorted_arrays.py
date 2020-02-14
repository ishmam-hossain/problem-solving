class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        res_node = ListNode(0)
        cur = res_node

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1 is not None:
            while l1:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
        if l2 is not None:
            while l2:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        return res_node.next


# l1_nxt_2 = ListNode(11)
l1_nxt_1 = ListNode(7)
ll1 = ListNode(5, l1_nxt_1)

# l2_nxt_3 = ListNode(9)
# l2_nxt_2 = ListNode(4, l2_nxt_3)
# l2_nxt_1 = ListNode(3, l2_nxt_2)
l2_nxt_1 = ListNode(3)
ll2 = ListNode(-9, l2_nxt_1)

s = Solution()
print(s.mergeTwoLists(ll1, ll2))

