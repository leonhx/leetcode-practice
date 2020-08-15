#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def gen_recur(self, leading_sets: List[List[int]], ns: List[List[int]]) \
            -> List[List[int]]:
        if not ns:
            return leading_sets
        all_sets = leading_sets[:]
        n, c = ns[0]
        for i in range(1, c + 1):
            all_sets += [s + [n] * i for s in leading_sets]
        return self.gen(all_sets, ns[1:])

    def gen_iter(self, ns: List[List[int]]) -> List[List[int]]:
        leading_sets = [[]]
        if not ns:
            return leading_sets
        for i in range(len(ns)):
            new_sets = leading_sets[:]
            n, c = ns[i]
            for rep in range(1, c + 1):
                new_sets += [s + [n] * rep for s in leading_sets]
            leading_sets = new_sets
        return leading_sets

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ns = []
        for n in nums:
            if not ns or n != ns[-1][0]:
                ns.append([n, 1])
            else:  # n == ns[-1][0]
                ns[-1][1] += 1
        return self.gen_iter(ns)
# @lc code=end
