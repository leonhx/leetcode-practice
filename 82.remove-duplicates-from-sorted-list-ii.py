#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        val = head.val
        if head.next.val == val:
            head = head.next
            while head and head.val == val:
                head = head.next
            return self.deleteDuplicates(head)
        else:
            remain = self.deleteDuplicates(head.next)
            head.next = remain
            return head
# @lc code=end
