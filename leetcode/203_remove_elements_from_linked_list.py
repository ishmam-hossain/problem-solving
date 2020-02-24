class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
    res_node = ListNode(0)
    res_node.next = head

    cur = head

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    if res_node.next.val == val:
        return res_node.next.next

    return res_node.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(6)

o = removeElements(node, 6)

r = o
while r:
    print(r.val)
    r = r.next
