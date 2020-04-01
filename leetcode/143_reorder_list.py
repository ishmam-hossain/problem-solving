# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        With additional space. Not in-place
        """
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next

        temp = ListNode(0)
        cur = temp
        for i in range(len(res)//2):
            cur.next = ListNode(res[i])
            cur.next.next = ListNode(res[len(res)-1-i])
            cur = cur.next.next
        if len(res) % 2 != 0:
            cur.next = ListNode(res[(len(res) // 2)])

        return temp.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = Solution()
data = s.reorderList(l)

while data:
    print(data.val, end=" ")
    data = data.next

