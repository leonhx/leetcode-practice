#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        if m > 1:
            head.next = self.reverseBetween(head.next, m - 1, n - 1)
            return head
        elif n > 1:
            prev = head
            x = ListNode(next=head.next)
            while n > 2 and x.next.next is not None:
                nxt2 = x.next.next
                x.next.next = prev
                prev = x.next
                x.next = nxt2
                n -= 1
            head.next = x.next.next
            x.next.next = prev
            return x.next
        else:
            return head
# @lc code=end
