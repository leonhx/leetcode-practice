#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        kth_node = head
        for _ in range(k - 1):
            if kth_node:
                kth_node = kth_node.next
        if not kth_node:
            return head
        next_head = self.reverseKGroup(kth_node.next, k)
        prev = head
        head = head.next
        prev.next = next_head
        while head != kth_node:
            n = head.next
            head.next = prev
            prev = head
            head = n
        kth_node.next = prev
        return kth_node
