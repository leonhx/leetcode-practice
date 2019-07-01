#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#
class Solution:
    def optional(self, f):
        def _f(s):
            try:
                r = f(s)
            except ValueError:
                r = None
            return (s, False) if r is None else (r, True)
        return _f

    def require(self, f):
        def _f(s):
            r = f(s)
            if r is None:
                self.raise_wrong_format()
            return r
        return _f

    def raise_wrong_format(self):
        raise ValueError('wrong format')

    def const_point(self, s: str) -> str:
        if s and s[0] == '.':
            return s[1:]
        return None

    def const_e(self, s: str) -> str:
        if s and s[0] == 'e':
            return s[1:]
        return None

    def const_sign(self, s: str) -> str:
        if s and (s[0] == '+' or s[0] == '-'):
            return s[1:]
        return None

    def either(self, *fns):
        def _f(s):
            for fn in fns:
                s, hit = self.optional(fn)(s)
                if hit:
                    return s
            return None
        return _f

    def digits(self, s: str) -> str:
        i = 0
        while i < len(s) and '0' <= s[i] <= '9':
            i += 1
        return None if i == 0 else s[i:]

    def unsigned_integer(self, s: str) -> str:
        if not s:
            return None
        if '0' <= s[0] <= '9':
            return self.optional(self.digits)(s[1:])[0]
        else:
            return None

    def signed_integer(self, s: str) -> str:
        s, _ = self.optional(self.const_sign)(s)
        return self.unsigned_integer(s)

    def floating(self, s: str) -> str:
        s, _ = self.optional(self.const_sign)(s)
        s, has_pre = self.optional(self.unsigned_integer)(s)
        s = self.require(self.const_point)(s)
        s, has_post = self.optional(self.unsigned_integer)(s)
        if not has_pre and not has_post:
            return None
        return s

    def exponential(self, s: str) -> str:
        s = self.require(self.either(self.floating, self.signed_integer))(s)
        s = self.require(self.const_e)(s)
        s = self.require(self.signed_integer)(s)
        return s

    def whitespace(self, s: str) -> str:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        return None if i == 0 else s[i:]

    def number(self, s: str) -> str:
        s, _ = self.optional(self.whitespace)(s)
        s = self.require(self.either(
            self.exponential, self.floating, self.signed_integer))(s)
        return self.optional(self.whitespace)(s)[0]

    def isNumber(self, s: str) -> bool:
        s, hit = self.optional(self.number)(s)
        return hit and not s
