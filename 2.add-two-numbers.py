#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.64%)
# Total Accepted:    779.4K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.carry: int = 0
        self.result: ListNode = None
        self.current: ListNode = None

        def add_digit(x):
            self.carry = x // 10
            x %= 10
            if self.result is None:
                self.result = ListNode(x)
                self.current = self.result
            else:
                self.current.next = ListNode(x)
                self.current = self.current.next
        while l1 is not None and l2 is not None:
            v = l1.val + l2.val + self.carry
            add_digit(v)
            l1 = l1.next
            l2 = l2.next
        lx = l1 if l1 else l2
        while lx is not None:
            v = lx.val + self.carry
            lx = lx.next
            add_digit(v)
        if self.carry > 0:
            add_digit(self.carry)
        return self.result


