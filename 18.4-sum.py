#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def __init__(self, debug=False):
        super().__init__()
        self.debug = debug

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if self.debug:
            print(f'nums: {nums}')
        s2_nums = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                n_i, n_j = nums[i], nums[j]
                s2_nums.setdefault(n_i + n_j, set()).add(((n_i, n_j), (i, j)))
        s2_nums = sorted(list(s2_nums.items()), key=lambda x: x[0])
        if self.debug:
            print(f's2_nums: {s2_nums}')
        results = set()
        i, j = 0, len(s2_nums) - 1
        while i <= j:
            (s1, x1s), (s2, x2s) = s2_nums[i], s2_nums[j]
            s_ = s1 + s2
            if s_ == target:
                for (x1_a, x1_b), (i1_a, i1_b) in x1s:
                    for (x2_a, x2_b), (i2_a, i2_b) in x2s:
                        if len({i1_a, i1_b, i2_a, i2_b}) == 4:
                            results.add(tuple(sorted([
                                x1_a, x1_b, x2_a, x2_b])))
                i += 1
                j -= 1
            elif s_ < target:
                i += 1
            else:
                j -= 1
        return list(results)
