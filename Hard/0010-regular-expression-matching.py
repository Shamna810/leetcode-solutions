"""
Notes:
- State: dp[i][j] = does s[:i] match p[:j]?
- '*' gives two choices: skip the "x*" pair (dp[i][j-2]) or
  consume one more char if it matches (dp[i-1][j]).
- Base case: empty string matches patterns like a*, a*b*, .*
- Edge cases: "aa" vs "a" (false), "ab" vs ".*" (true)
- Time: O(m*n), Space: O(m*n)
"""

# 10. Regular Expression Matching
# Difficulty: Hard
# Link: https://leetcode.com/problems/regular-expression-matching/
# Approach: Bottom-up dynamic programming
# Time: O(m * n)   Space: O(m * n)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Empty string can match patterns like a*, a*b*, .*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Case 1: use zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: use one or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    # Normal character or '.'
                    if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]