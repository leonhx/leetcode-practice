#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_head = less_cur = ListNode()
        remain_head = remain_cur = ListNode()
        while head is not None:
            if head.val < x:
                less_cur.next = head
                less_cur = head
            else:
                remain_cur.next = head
                remain_cur = head
            head = head.next
        remain_cur.next = None
        less_cur.next = remain_head.next
        return less_head.next
# @lc code=end
