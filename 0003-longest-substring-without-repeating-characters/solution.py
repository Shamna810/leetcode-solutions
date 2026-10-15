class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # char -> most recent index
        left = 0         # start of current window
        best = 0

        for right, ch in enumerate(s):
            # If ch is already inside the window, shrink the window past it
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best