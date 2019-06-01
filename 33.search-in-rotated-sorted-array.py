#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def binarySearch(self, l_i: int, r_i: int) -> int:
        if l_i > r_i:
            return -1
        m_i = (r_i + l_i) // 2
        l, m, r = self.nums[l_i], self.nums[m_i], self.nums[r_i]
        if m == self.target:
            return m_i
        elif l == self.target:
            return l_i
        elif r == self.target:
            return r_i
        elif self.target > m:
            if l > m and self.target > l:
                return self.binarySearch(l_i + 1, m_i - 1)
            else:
                return self.binarySearch(m_i + 1, r_i - 1)
        else:
            if r < m and self.target < r:
                return self.binarySearch(m_i + 1, r_i - 1)
            else:
                return self.binarySearch(l_i + 1, m_i - 1)

    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.binarySearch(0, len(nums) - 1)
