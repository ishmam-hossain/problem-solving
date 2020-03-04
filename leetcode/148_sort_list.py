# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        stack.sort()
        res_node = ListNode(0)
        cur = res_node
        i = 0
        while i < len(stack):
            cur.next = ListNode(stack[i])
            cur = cur.next
            i += 1

        return res_node.next
