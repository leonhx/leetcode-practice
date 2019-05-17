#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            n_left = len(nums) // 2
            n = TreeNode(nums[n_left])
            n.left = self.sortedArrayToBST(nums[:n_left])
            n.right = self.sortedArrayToBST(nums[n_left + 1:])
            return n
