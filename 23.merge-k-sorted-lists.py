#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root, current = None, None
        lists = [l for l in lists if l]
        while lists:
            lists.sort(key=lambda l: l.val)
            n = ListNode(lists[0].val)
            lists[0] = lists[0].next
            lists = [l for l in lists if l]
            if root is None:
                root = n
                current = n
            else:
                current.next = n
                current = current.next
        return root
