# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        res = head
        while res:
            stack.append(res.val)
            res = res.next

        while head:
            cur_val = stack.pop()
            if head.val != cur_val:
                return False
            head = head.next

        return True