#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        val = postorder[-1]
        i = len(inorder) - 1
        while i >= 0 and inorder[i] != val:
            i -= 1
        right_i = i - len(inorder)
        return TreeNode(
            val=val,
            left=self.buildTree(inorder[:i], postorder[:right_i]),
            right=self.buildTree(inorder[i + 1:], postorder[right_i:-1]))
# @lc code=end
