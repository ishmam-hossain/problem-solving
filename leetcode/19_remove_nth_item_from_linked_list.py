# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        total_nodes = 0
        cur = head
        while cur:
            total_nodes += 1
            cur = cur.next

        cur = head

        n = total_nodes - n
        if n == 0:
            return head.next

        pos = 1
        while cur.next:
            if pos == n:
                cur.next = cur.next.next
                break
            cur = cur.next
            pos += 1
        if pos > 0:
            return head
        else:
            return head.next