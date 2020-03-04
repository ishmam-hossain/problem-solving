class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_ll(head: ListNode) -> ListNode:
    if not head:
        return ListNode(0).next

    # return head
    cur = head
    nxt = head.next
    later = head.next.next

    while cur:
        if cur.next.next:
            nxt.next = cur
            nxt = cur.next
            cur = later
            later = cur.next.next
            print(cur.val, nxt.val)


my_list = ListNode(1)
my_list.next = ListNode(2)
my_list.next.next = ListNode(3)
my_list.next.next.next = ListNode(4)

r = reverse_ll(my_list)

while r:
    print(r.val, end=" -> ")
    r = r.next
