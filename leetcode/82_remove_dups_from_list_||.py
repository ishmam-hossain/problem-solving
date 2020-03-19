# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_duplicates(self, stack):
        l = len(stack)
        if l == 1:
            return stack
        new_stack = []

        for i, n in enumerate(stack):
            if i == 0 and i+1 < l and stack[i + 1] != n:
                new_stack.append(n)
                continue
            if i == l - 1 and i - 1 >= 0 and stack[i - 1] != n:
                new_stack.append(n)
                continue
            if stack[i - 1] != n and stack[i + 1] != n:
                new_stack.append(n)
        return new_stack

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        res = ListNode(0)
        cur = res
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        new_stack = self.remove_duplicates(stack)

        for v in new_stack:
            cur.next = ListNode(v)
            cur = cur.next

        return res.next
