#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
class Solution:
    def __init__(self, debug=False):
        self.d = debug

    def minWindow(self, s: str, t: str) -> str:
        i, j, counter, res = 0, 0, {}, None
        for c in t:
            counter.setdefault(c, 0)
            counter[c] += 1
        if self.d:
            print(f'counter: {counter}')
        while j < len(s):
            match = False
            while j < len(s):
                c = s[j]
                j += 1
                if c in counter:
                    counter[c] -= 1
                    match = counter[c] <= 0 and all([
                        v <= 0 for v in counter.values()])
                    if match: break
            if not match: break
            if self.d:
                print(f'j={j}: {s[i:j]}, {counter}')
            while i < j:
                c = s[i]
                if c in counter:
                    if counter[c] < 0:
                        counter[c] += 1
                    else:
                        if res is None or len(res) > j - i:
                            res = s[i:j]
                        break
                i += 1
        return '' if res is None else res
