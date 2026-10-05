"""
4. Median of Two Sorted Arrays (Hard)
https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach: binary search on the partition of the shorter array.
Time:  O(log(min(m, n)))
Space: O(1)
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2  # elements taken from nums1 for the left half
            j = half - i        # elements taken from nums2 for the left half

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                hi = i - 1  # took too many from nums1
            else:
                lo = i + 1  # took too few from nums1
