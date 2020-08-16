#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gen(self, n: int, i: int) -> List[TreeNode]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(val=i)]
        trees = []
        for left_n in range(n):
            left_trees = self.gen(left_n, i)
            right_trees = self.gen(n - left_n - 1, i + left_n + 1)
            for left in left_trees:
                for right in right_trees:
                    trees.append(TreeNode(
                        val=i + left_n, left=left, right=right))
        return trees

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.gen(n, 1)
# @lc code=end
