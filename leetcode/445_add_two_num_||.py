# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_num(self.get_digits(l1))
        num2 = self.get_num(self.get_digits(l2))

        return self.make_list(num1 + num2)

    def get_digits(self, node):
        stack = []
        while node:
            stack.append(node.val)
            node = node.next

        return stack

    def get_num(self, lst):
        _sum = i = 0
        for n in reversed(lst):
            _sum += n * 10 ** i
            i += 1
        return _sum

    def make_list(self, num):
        res = ListNode(0)
        if num == 0:
            return res
        cur = res
        stack = []
        while num:
            digit = num % 10
            stack.append(digit)
            num //= 10

        while stack:
            cur.next = ListNode(stack.pop())
            cur = cur.next
        return res.next


x = ListNode(7)
x.next = ListNode(2)
x.next.next = ListNode(4)
x.next.next.next = ListNode(3)

y = ListNode(5)
y.next = ListNode(6)
y.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(x, y))
