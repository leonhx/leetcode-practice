#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = [[i] for i in range(1, n + 2 - k)]
        for i in range(1, k):
            combs_x = []
            for cb in combs:
                for x in range(cb[-1] + 1, n - k + i + 2):
                    combs_x.append(cb[:] + [x])
            combs = combs_x
        return combs
# @lc code=end
