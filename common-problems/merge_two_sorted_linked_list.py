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


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    res = SinglyLinkedListNode(0)
    cur = res
    while head1 and head2:
        if head1.data > head2.data:
            cur.next = SinglyLinkedListNode(head2.data)
            cur = cur.next
            head2 = head2.next
        elif head1.data < head2.data:
            cur.next = SinglyLinkedListNode(head1.data)
            cur = cur.next
            head1 = head1.next
        else:
            cur.next = SinglyLinkedListNode(head1.data)
            cur.next.next = SinglyLinkedListNode(head2.data)
            head1 = head1.next
            head2 = head2.next
            cur = cur.next.next

    if head1:
        cur.next = head1
    if head2:
        cur.next = head2

    return res.next

