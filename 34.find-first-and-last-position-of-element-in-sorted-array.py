#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    LEFT_MOST = 'left_most'
    RIGHT_MOST = 'right_most'
    ANY = 'any'

    def binarySearch(self, li: int, ri: int, which: str = None) -> int:
        if li > ri:
            return -1
        which = which or Solution.ANY
        mi = (li + ri) // 2
        m = self.ns[mi]
        if m == self.t:
            if which == Solution.LEFT_MOST and mi > 0 \
                    and self.ns[mi - 1] == self.t:
                return self.binarySearch(li, mi - 1, which)
            elif which == Solution.RIGHT_MOST and mi < len(self.ns) - 1 \
                    and self.ns[mi + 1] == self.t:
                return self.binarySearch(mi + 1, ri, which)
            else:
                return mi
        elif m < self.t:
            return self.binarySearch(mi + 1, ri, which)
        else:
            return self.binarySearch(li, mi - 1, which)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.ns = nums
        self.t = target
        return [
            self.binarySearch(0, len(nums) - 1, Solution.LEFT_MOST),
            self.binarySearch(0, len(nums) - 1, Solution.RIGHT_MOST)
        ]
