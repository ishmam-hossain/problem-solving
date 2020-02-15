# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:
    def iterative_reverse_list(self, head: ListNode) -> ListNode:
        res_node = ListNode(0)
        cur_node = res_node
        node_stack = []

        while head is not None:
            node_stack.append(head.val)
            head = head.next

        while node_stack:
            cur_node.next = ListNode(node_stack.pop())
            cur_node = cur_node.next

        return res_node.next



