# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode):
        if not head or not head.next:
            return ListNode(-1)

        slow = fast = head

        while fast.next and fast.next.next:
            if slow is fast:
                return slow.val
            if not slow.next or not fast.next.next:
                return ListNode(-1)

            slow = slow.next
            fast = fast.next.next

        return ListNode(-1)


n1 = ListNode(1)
# n1.next = ListNode(2)
# n1.next.next = n1
# n1.next.next.next = ListNode(1)

s = Solution()
print(s.detectCycle(n1))
