#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _deleteNode(self, head: ListNode, val) -> ListNode:
        if head is None:
            return head
        if val is not None and val == head.val:
            return self._deleteNode(head.next, val)
        head.next = self._deleteNode(head.next, head.val)
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        return self._deleteNode(head, None)
