"""
59. Spiral Matrix II (Medium)

Approach: Boundary shrinking
- Keep four boundaries: top, bottom, left, right.
- Fill top row (L->R), right column (T->B), bottom row (R->L),
  left column (B->T), then move each boundary inward.
- The `if` checks before the last two loops prevent overwriting
  cells when n is odd (center cell).

Time:  O(n^2) - every cell is filled once
Space: O(n^2) - output matrix (O(1) extra)
"""

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1

        while top <= bottom and left <= right:
            # Left -> Right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Top -> Bottom along the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Right -> Left along the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # Bottom -> Top along the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix