#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k: int = len(nums1) - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            n1, n2 = nums1[m], nums2[n]
            if n1 > n2:
                nums1[k] = n1
                k -= 1
                m -= 1
            else:
                nums1[k] = n2
                k -= 1
                n -= 1
        rem_nums, rem_i = (nums1, m) if m >= 0 else (nums2, n)
        while rem_i >= 0:
            nums1[k] = rem_nums[rem_i]
            k -= 1
            rem_i -= 1
        if k >= 0:
            i = 0
            k += 1
            while k < len(nums1):
                nums1[i] = nums1[k]
                i += 1
                k += 1
            while i < len(nums1):
                nums1[i] = 0
                i += 1

