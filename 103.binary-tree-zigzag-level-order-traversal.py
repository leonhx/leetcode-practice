#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        reverse = False
        trees = [root]
        while trees:
            level_order = [t.val for t in trees]
            if reverse:
                level_order = level_order[::-1]
            result.append(level_order)
            reverse = not reverse

            new_trees = []
            for t in trees:
                if t.left is not None:
                    new_trees.append(t.left)
                if t.right is not None:
                    new_trees.append(t.right)
            trees = new_trees
        return result
# @lc code=end
