#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2020/1/3 8:59 PM
 @Author  : Qiang,Q
 @File    : 2_add_two_numbers.py
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
        self.val = x
        self.next = None




class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        tail = res
        carry = 0
        while(l1 or l2 or carry != 0):
            if((l1 is None or l2 is None) and carry == 0):
                if l1 is None:tail.next = l2
                if l2 is None:tail.next = l1

            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val
            sum = v1 + v2 + carry
            carry = sum // 10
            val = sum % 10
            tail.next = ListNode(val)
            tail = tail.next

            l1 = None if  l1 is None else l1.next
            l2 = None if l2 is None else l2.next


        return res.next



if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)
    # n7 = ListNode(2)

    n4.next = n5
    n5.next = n6
    # n6.next = n7



    s = Solution()
    res = s.addTwoNumbers(n1,n4)
    while(res is not None):
        print(res.val)
        res = res.next

