#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _rm_nth(self, head: ListNode, n: int):
        if not head:
            return head, 0
        head_, n_ = self._rm_nth(head.next, n)
        if n == n_:
            if head_:
                head.next = head_.next
            else:
                head = None
        return head, n_ + 1

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head_, n_ = self._rm_nth(head, n)
        if n_ == n:
            head_ = head_.next
        return head_
