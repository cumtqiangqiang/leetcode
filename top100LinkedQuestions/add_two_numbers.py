#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2020/1/3 8:59 PM
 @Author  : Qiang,Q
 @File    : add_two_numbers.py
 @Software: PyCharm Community Edition
'''
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


def addTwoNumbers(self, l1: ListNode, l2: ListNode):
   n, r = divmod(l1.value + l2.value, 10)
   l1, l2 = l1.next, l2.next
   head = node = ListNode(r)

   while l1 or l2:
       if l1 and l2:
           n, r = divmod(l1.value + l2.value + n, 10)
       elif l1:
           n, r = divmod(l1.value + l2.value + n, 10)
           l1 = l1.next
       else:
           n, r = divmod(l2.value + n, 10)
           l2 = l2.next
       node.next = ListNode(r)
       node = node.next
    if n:
        node.next = ListNode(n)
        node = node.next

    return  head
if __name__ == '__main__':
    list_node1 = ListNode(2)
    list_node2 = ListNode(4)
    list_node3 = ListNode(3)
    list_node1.next = list_node2
    list_node2.next = list_node3

    l = list_node1
    while(l.next != None):
        print(l.value)
        l = l.next



