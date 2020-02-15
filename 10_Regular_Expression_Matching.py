class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memoize = [[None for _ in p] for _ in s]

        def recurseIsMatch(s_i, p_i):
            if (p_i == len(p) and s_i == len(s)):
                return True

            if (p_i == len(p)):
                return False

            if s_i < len(s) and p_i < len(p) and self.memoize[s_i][p_i] is not None:
                return self.memoize[s_i][p_i]

            match = False
            if (p_i + 1 < len(p) and p[p_i + 1] == '*'):
                if (s_i < len(s) and (s[s_i] == p[p_i] or p[p_i] == '.')):
                    match = match or recurseIsMatch(s_i + 1, p_i + 2) or recurseIsMatch(s_i + 1, p_i)
                match = match or recurseIsMatch(s_i, p_i + 2)
            elif (s_i < len(s) and s[s_i] == p[p_i] or p[p_i] == '.'):
                match = match or recurseIsMatch(s_i + 1, p_i + 1)

            if s_i < len(s) and p_i < len(p):
                self.memoize[s_i][p_i] = match
            return match

        return recurseIsMatch(0, 0)


assert (Solution().isMatch("aa", "a") == False)
assert (Solution().isMatch("aa", "a") == False)
assert (Solution().isMatch("aa", "a*") == True)
assert (Solution().isMatch("aab", "a*") == False)
assert (Solution().isMatch("aab", "a*b*") == True)
assert (Solution().isMatch("aaaaa", "aaaaaa") == False)
assert (Solution().isMatch("aaaaa", ".**") == False)
assert (Solution().isMatch("aaaaa", ".*.*") == True)
assert (Solution().isMatch("aa", "a*a*") == True)
assert (Solution().isMatch("aa", "a*a*a*") == True)
assert (Solution().isMatch("aab", "c*a*b") == True)
assert (Solution().isMatch("mississippi", "mis*is*p*.") == False)
assert (Solution().isMatch("ab", ".*") == True)
assert (Solution().isMatch("a", "ab*") == True)
