"""
LeetCode 85. Maximal Rectangle - Dynamic Programming approach

For each row, maintain per column:
    height[j]: consecutive 1s above (and including) this cell
    left[j]:   leftmost index the rectangle of height[j] can extend to
    right[j]:  rightmost boundary (exclusive) it can extend to
Area at column j = height[j] * (right[j] - left[j])

Time:  O(rows * cols)
Space: O(cols)
"""
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        height = [0] * cols
        left = [0] * cols
        right = [cols] * cols
        best = 0

        for row in matrix:
            cur_left, cur_right = 0, cols

            for j in range(cols):
                height[j] = height[j] + 1 if row[j] == "1" else 0

            for j in range(cols):
                if row[j] == "1":

                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in range(cols - 1, -1, -1):
                if row[j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = cols
                    cur_right = j

            for j in range(cols):
                best = max(best, height[j] * (right[j] - left[j]))

        return best