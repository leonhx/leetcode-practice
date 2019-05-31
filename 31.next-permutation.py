#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def __init__(self, debug=False):
        self.debug = debug

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pi = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                # found
                si, ei = i - 1, i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        ei = j
                    else:
                        break
                if self.debug:
                    print(si, ei)
                nums[si], nums[ei] = nums[ei], nums[si]
                pi = si + 1
                break
        ei = len(nums) - 1
        while pi < ei:
            nums[pi], nums[ei] = nums[ei], nums[pi]
            pi += 1
            ei -= 1
        if self.debug:
            print(nums)
