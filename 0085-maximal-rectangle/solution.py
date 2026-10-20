from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # extra 0 at the end acts as a sentinel
        best = 0

        for row in matrix:
            # Update histogram heights for this row
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0

            # Largest rectangle in histogram using a monotonic stack
            stack = [-1]
            for j in range(cols + 1):
                while stack[-1] != -1 and heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    best = max(best, h * w)
                stack.append(j)

        return best