# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = []
        for lst in lists:
            tmp = self.get_list(lst)
            result.extend(tmp)

        result.sort()

        res = ListNode(0)
        cur = res
        for node in result:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next

    def get_list(self, head):
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next

        return temp