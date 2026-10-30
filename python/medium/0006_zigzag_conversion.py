"""
6. Zigzag Conversion (Medium)
https://leetcode.com/problems/zigzag-conversion/

Approach: Simulate the zigzag with one bucket per row.
  - Walk through the string once, appending each character to the current row.
  - Bounce direction when we reach the top row or the bottom row.
  - Join all rows at the end.

Time:  O(n)  - each character is visited once
Space: O(n)  - the row buckets hold all n characters
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # No zigzag possible: return the string as is
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur, step = 0, 1

        for c in s:
            rows[cur] += c
            # Reverse direction at the top and bottom rows
            if cur == 0:
                step = 1
            elif cur == numRows - 1:
                step = -1
            cur += step

        return "".join(rows)