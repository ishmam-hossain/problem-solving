# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            head.val, head.next.val = head.next.val, head.val
            self.swapPairs(head.next.next)

        return head


my_list = ListNode(1)
my_list.next = ListNode(2)
my_list.next.next = ListNode(3)
my_list.next.next.next = ListNode(4)
# data = my_list
s = Solution()
data = s.swapPairs(my_list)
while data is not None:
    print(data.val)
    data = data.next
