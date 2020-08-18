#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = []
        trees = [root]
        while trees:
            result.append([t.val for t in trees])
            new_trees = []
            for t in trees:
                if t.left is not None:
                    new_trees.append(t.left)
                if t.right is not None:
                    new_trees.append(t.right)
            trees = new_trees
        return result
# @lc code=end
