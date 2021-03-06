#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None
        elif q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)
