#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])
        val = preorder[0]
        i = 0
        while i < len(inorder) and inorder[i] != val:
            i += 1
        left_tree = self.buildTree(preorder[1:i + 1], inorder[:i])
        right_tree = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return TreeNode(val=val, left=left_tree, right=right_tree)
# @lc code=end
