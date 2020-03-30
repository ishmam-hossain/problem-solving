#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    pos = 0
    cur = head

    while cur:
        if pos == position - 1:
            nxt_node = cur.next
            cur.next = SinglyLinkedListNode(data)
            cur.next.next = nxt_node
            break
        cur = cur.next
        pos += 1

    return head


if __name__ == '__main__':
    l = SinglyLinkedListNode(16)
    l.next = SinglyLinkedListNode(13)
    l.next.next = SinglyLinkedListNode(7)

    res = insertNodeAtPosition(l, 1, 2)
    while res:
        print(res.data)
        res = res.next
