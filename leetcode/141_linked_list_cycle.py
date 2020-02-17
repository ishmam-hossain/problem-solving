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


s = Solution()
print(s.hasCycle(ListNode(1)))
