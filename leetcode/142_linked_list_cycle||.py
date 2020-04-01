# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = []
        while head:
            if head in visited:
                return head
            visited.append(head)
            head = head.next

        return