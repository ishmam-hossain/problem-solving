
# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position == 0:
        return head.next

    pos = 0
    cur = head

    while cur.next:
        if pos == position - 1:
            cur.next = cur.next.next
            break
        cur = cur.next
        pos += 1

    return head
