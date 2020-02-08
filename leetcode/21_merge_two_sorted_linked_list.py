# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # while l1 or l2:
        #     try:
        #         l1 = l1.next
        #         print(l1.val, l2.val)
        #     except AttributeError:
        #         l1 = None
        #     try:
        #         l2 = l2.next
        #     except AttributeError:
        #         l2 = None

        ll1 = []
        while l1:
            ll1.append(l1.val)
            l1 = l1.next
        print(ll1)

        ll2 = []
        while l2:
            ll2.append(l2.val)
            l2 = l2.next

        print(ll2)


l1_nxt_2 = ListNode(11)
l1_nxt_1 = ListNode(2, l1_nxt_2)
l1 = ListNode(1, l1_nxt_1)

l2_nxt_3 = ListNode(9)
l2_nxt_2 = ListNode(4, l2_nxt_3)
l2_nxt_1 = ListNode(3, l2_nxt_2)
l2 = ListNode(1, l2_nxt_1)

s = Solution()
print(s.mergeTwoLists(l1, l2))
