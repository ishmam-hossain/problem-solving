# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_linked_list(arr):
    res_node = ListNode(0)
    cur_node = res_node

    while arr:
        cur_node.next = ListNode(arr.pop())
        cur_node = cur_node.next

    return res_node.next


def PRINT(d):
    if d is None:
        return
    PRINT(d.next)
    print('-> ', end='')
    print(d.val, end=' ')
# -----------------------------------------------


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur_node = head

        while cur_node is not None and cur_node.next is not None:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return head


s = Solution()
ll = make_linked_list([1, 1, 2, 3, 3])
ll2 = make_linked_list([1, 2, 3, 3, 3, 5, 6, 6])
PRINT(s.deleteDuplicates(ll))

print('\n------------------')
PRINT(s.deleteDuplicates(ll2))
