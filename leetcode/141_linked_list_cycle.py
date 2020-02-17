# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur_node = head
        visited = []
        while cur_node:
            if cur_node in visited:
                return True
            visited.append(cur_node)
            cur_node = cur_node.next

        return False

    def has_cycle_constant_space_complexity(self, head: ListNode) -> bool:
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


s = Solution()
print(s.hasCycle(ListNode(1)))
print(s.has_cycle_constant_space_complexity(ListNode(1)))
