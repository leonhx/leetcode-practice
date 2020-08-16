#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def is_valid(self, s: str) -> bool:
        return 0 <= int(s) <= 255 and (len(s) == 1 or s[0] != '0')

    def restore(self, s: str, n: int) -> List[str]:
        if not s:
            return []
        if n == 1:
            return [s] if self.is_valid(s) else []
        results = []
        for j in range(min(len(s), 3)):
            if self.is_valid(s[:j + 1]):
                sub_results = self.restore(s[j + 1:], n - 1)
                results += [s[:j + 1] + '.' + sub for sub in sub_results]
            else:
                break
        return results

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restore(s, 4)
# @lc code=end
