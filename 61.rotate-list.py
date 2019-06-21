#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, head: ListNode) -> int:
        return 1 + self.length(head.next) if head else 0

    def length2(self, head: ListNode) -> int:
        n = 0
        while head:
            head = head.next
            n += 1
        return n

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = self.length2(head)
        if n == 0:
            return head
        k %= n
        if k == 0:
            return head
        node = head
        for _ in range(n - k - 1):
            node = node.next
        new_head, node.next = node.next, None
        node = new_head
        while node.next:
            node = node.next
        node.next = head
        return new_head
