class SolutionOptimized:
    """
    Sliding window with last-seen index map.

    Idea:
        Keep a window [left, right] with no repeated characters.
        If s[right] was seen at an index >= left, jump left to just
        past that previous occurrence instead of shrinking step by step.

    Time:  O(n)          - each character is processed once
    Space: O(min(n, k))  - k is the size of the character set
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best