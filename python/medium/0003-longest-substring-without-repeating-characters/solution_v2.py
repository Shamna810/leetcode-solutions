"""
LeetCode 3 - Version 2: array instead of dict

Same sliding window idea, but uses a fixed-size list indexed by
ASCII code instead of a hash map. This avoids hashing overhead
and gives O(1) space, since the table size is constant.

Assumes ASCII input, which matches the problem constraints.

Time:  O(n)
Space: O(1) - fixed 256-element table
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 256   # last index of each character
        left = 0
        best = 0

        for right, ch in enumerate(s):
            code = ord(ch)
            if last[code] >= left:
                left = last[code] + 1
            last[code] = right
            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    print("v2 tests passed")