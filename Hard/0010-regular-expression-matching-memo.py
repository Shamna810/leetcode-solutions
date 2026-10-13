# 10. Regular Expression Matching (Alternative: Top-down memoization)
# Difficulty: Hard
# Link: https://leetcode.com/problems/regular-expression-matching/
# Approach: Recursion + caching. Only computes states that are reachable.
# Time: O(m * n)   Space: O(m * n)

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            first = i < len(s) and p[j] in (s[i], '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                return dfs(i, j + 2) or (first and dfs(i + 1, j))
            return first and dfs(i + 1, j + 1)

        return dfs(0, 0)